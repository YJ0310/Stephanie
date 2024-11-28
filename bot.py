import os
import io
import base64
import telebot
from telebot import TeleBot
from openai import OpenAI
from PIL import Image
from config import Config
from image_processing import process_image
from sticker_processing import process_sticker, download_sticker
from reserved_output import BotOutput

class TelegramBot:
    def __init__(self):
        self.bot = TeleBot(Config.TELEGRAM_BOT_TOKEN)
        self.openai_client = OpenAI(api_key=Config.OPENAI_API_KEY)

        # Register message handlers
        self.bot.message_handler(commands=["start", "help"])(self.send_welcome)
        self.bot.message_handler(
            content_types=["photo", "document", "text", "sticker"]
        )(self.handle_message)

    def download_file(self, file_info):
        """Download file from Telegram servers."""
        return self.bot.download_file(file_info.file_path)

    def send_welcome(self, message):
        """Handle start and help commands."""
        self.bot.reply_to(message, BotOutput.WELCOME_MESSAGE)

    def generate_ai_response(self, message):
        """Generate AI response using OpenAI."""
        try:
            response = self.openai_client.chat.completions.create(
                model=Config.MODEL,
                messages=[
                    {"role": "system", "content": BotOutput.Prompts.DEFAULT_SYSTEM},
                    {"role": "user", "content": message},
                ],
                store=True
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            return BotOutput.Errors.OPENAI_ERROR

    def handle_message(self, message):
        """Handle incoming messages."""
        # Handle text messages
        if message.text:
            ai_response = self.generate_ai_response(message.text)
            self.bot.reply_to(message, ai_response)
            return

        # Handle image messages
        image_data = None
        ai_response = None

        if message.photo:
            # Get the largest available photo
            file_info = self.bot.get_file(message.photo[-1].file_id)
            downloaded_file = self.download_file(file_info)
            image_data = downloaded_file

        # Handle document messages
        elif message.document:
            file_info = self.bot.get_file(message.document.file_id)
            downloaded_file = self.download_file(file_info)

            # Check if it's an image
            try:
                Image.open(io.BytesIO(downloaded_file))
                image_data = downloaded_file
            except Exception:
                # If not an image, treat as a document
                self.bot.reply_to(message, BotOutput.Errors.DOCUMENT_ERROR)
                return

        # Handle sticker messages
        elif message.sticker:
            file_info = self.bot.get_file(message.sticker.file_id)
            sticker_path = download_sticker(self.bot, file_info)

            if sticker_path:
                # Process the sticker
                ai_response = process_sticker(sticker_path, self.openai_client)

                # Clean up the downloaded sticker
                try:
                    os.remove(sticker_path)
                except Exception as e:
                    print(f"Error removing sticker file: {e}")

        # Process image if available
        if image_data:
            ai_response = process_image(image_data, self.openai_client)

        # Reply with the generated response
        if ai_response:
            self.bot.reply_to(message, ai_response)

    def start(self):
        """Start the bot."""
        print(BotOutput.Status.BOT_RUNNING)
        self.bot.polling(none_stop=True)
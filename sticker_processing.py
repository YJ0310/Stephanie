import os
import base64
from openai import OpenAI
from config import Config
from reserved_output import BotOutput

def process_sticker(file_path, openai_client):
    """
    Process a sticker using OCR or image analysis
    
    Args:
        file_path (str): Path to the downloaded sticker file
        openai_client (OpenAI): OpenAI client for processing
    
    Returns:
        str: Analysis or description of the sticker
    """
    try:
        # Read the sticker file
        with open(file_path, 'rb') as sticker_file:
            # Use OpenAI vision to analyze the sticker
            response = openai_client.chat.completions.create(
                model=Config.MODEL,
                messages=[
                    {"role": "system", "content": BotOutput.Prompts.IMAGE_ANALYSIS},
                    {"role": "user", "content": [
                        {"type": "text", "text": "What can you tell me about this sticker?"},
                        {"type": "image", "image_url": {"url": f"data:image/png;base64,{base64.b64encode(sticker_file.read()).decode()}"}}
                    ]}
                ]
            )
            return response.choices[0].message.content
    except Exception as e:
        print(f"Sticker processing error: {e}")
        return BotOutput.Errors.STICKER_PROCESSING_ERROR

def download_sticker(bot, file_info):
    """
    Download a sticker from Telegram servers
    
    Args:
        bot (TeleBot): Telegram bot instance
        file_info (FileInfo): Telegram file information
    
    Returns:
        str: Path to the downloaded sticker file
    """
    try:
        # Create a directory for stickers if it doesn't exist
        os.makedirs('stickers', exist_ok=True)
        
        # Generate a unique filename
        file_path = os.path.join('stickers', f"{file_info.file_id}.png")
        
        # Download the sticker
        downloaded_file = bot.download_file(file_info.file_path)
        
        # Save the sticker
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        return file_path
    except Exception as e:
        print(f"Sticker download error: {e}")
        return None
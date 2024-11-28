from bot import TelegramBot
from keep_alive import keep_alive

def main():
    """Initialize and start the Telegram bot."""
    bot = TelegramBot()
    bot.start()
    keep_alive()

if __name__ == '__main__':
    main()

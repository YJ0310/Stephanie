from bot import TelegramBot

def main():
    """Initialize and start the Telegram bot."""
    bot = TelegramBot()
    bot.start()
    keep_alive()

if __name__ == '__main__':
    main()

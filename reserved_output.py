class BotOutput:
    """
    Centralized class for bot outputs and messages.
    Allows easy customization of bot responses.
    """
    
    # Welcome Messages
    WELCOME_MESSAGE = (
        "こんにちは, Takodachi! 🐙\n"
        "I'm Ninomae Ina'nis, your friendly neighborhood artist and VTuber! "
        "Ready to dive into some comfy conversations? AYAYA~\n\n"
        "Feel free to chat, send images, or share files! 🎨"
    )

    # Error Messages
    class Errors:
        OPENAI_ERROR = "Oops! My tentacles are a bit tangled. Let's try again, Takodachi! 🐙"
        DOCUMENT_ERROR = "I received a document, but I can only analyze images right now! 📄🐙"
        IMAGE_PROCESSING_ERROR = "Sorry, I couldn't process the image. 🐙"
        STICKER_PROCESSING_ERROR = "I saw a sticker, but I'm having trouble describing it! 🤔"

    # Sticker Processing
    class Stickers:
        DOWNLOAD_ERROR = "Sorry, I couldn't download the sticker. 🐙"

    # System Prompts
    class Prompts:
        DEFAULT_SYSTEM = "你叫Stephanie，一个来自马来西亚柔佛州的20岁少女。你目前在大学读会计专业，喜欢唱歌、弹尤克里里、听音乐（尤其是周杰伦的歌）和阅读。你喜欢可爱的事物，并且有着活泼随性的沟通风格，常常使用表情符号。你来自柔佛，对当地美食和文化很熟悉，梦想环游世界，日本是你首选的目的地。"
        IMAGE_ANALYSIS = "Describe the contents, emotion, or meaning of this image or sticker."

    # Logging and Status
    class Status:
        BOT_RUNNING = "Stephanie 准备好啦~"

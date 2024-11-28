# config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Telegram Bot Configuration
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # MongoDB Configuration
    MONGODB_URI = os.getenv('MONGODB_URI')
    
    # model Configuration
    MODEL = os.getenv('MODEL')
    
    # Additional configurations can be added here
    
# # Voice model paths
# VOICE_MODEL_CKPT = r"C:\Users\yinji\Downloads\Ninomae Inanis-e10.ckpt"
# VOICE_MODEL_PTH = r"C:\Users\yinji\Downloads\Ninomae Inanis_e8_s104.pth"

# mongodb password: 8xo5ZiXLjWaWZMGF
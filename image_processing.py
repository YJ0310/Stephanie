import base64
from openai import OpenAI
from config import Config

def process_image(file, openai_client):
    """Process image using OpenAI's vision capabilities."""
    try:
        # Send image to OpenAI Vision API
        response = openai_client.chat.completions.create(
            model=Config.MODEL,
            messages=[
                {"role": "system", "content": "Analyze this image creatively."},
                {"role": "user", "content": [
                    {"type": "text", "text": "What can you tell me about this image?"},
                    {"type": "image", "image_url": {"url": f"data:image/jpeg;base64,{base64.b64encode(file).decode()}"}}
                ]}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Image processing error: {e}")
        return "Sorry, I couldn't process the image. 🐙"

import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    open_ai_key = os.getenv('OPENAI_KEY')
    print("Hello, World!")
    print(open_ai_key)
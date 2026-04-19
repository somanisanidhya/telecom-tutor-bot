import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
model = os.environ.get("MODEL_NAME", "llama-3.3-70b-versatile")

print(f"Testing model: {model}")
client = Groq(api_key=api_key)

try:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": "Say hello"}
        ]
    )
    print("Success!")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")

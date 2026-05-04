import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")

api_key = os.getenv("DEEPGRAM_API_KEY")
url = "https://api.deepgram.com/v1/speak?model=aura-2-andromeda-en"

payload = {
    "text": "Hello, this is a Deepgram test."
}
headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json"
}

print(f"Testing Deepgram API with key: {api_key[:5]}...")
try:
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success! Deepgram works.")
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Exception: {e}")

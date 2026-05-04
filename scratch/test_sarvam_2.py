import requests
import os
from dotenv import load_dotenv

# Use the dashboard .env key
api_key = "sk_ep68lfyw_WJjKSP7dkmOT71Vy4B1RhJTD"
url = "https://api.sarvam.ai/text-to-speech"

payload = {
    "text": "నమస్కారం, ఇది ఒక పరీక్ష.",
    "target_language_code": "te-IN",
    "speaker": "anushka",
    "model": "bulbul:v2"
}
headers = {
    "api-subscription-key": api_key,
    "Content-Type": "application/json"
}

print(f"Testing Sarvam API with key: {api_key[:10]}...")
try:
    response = requests.post(url, json=payload, headers=headers, timeout=20)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success! Audio data received.")
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Exception: {e}")

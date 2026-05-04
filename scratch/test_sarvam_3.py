import requests
import os
from dotenv import load_dotenv

api_key = "sk_mf1qdfiu_hxy11vkzaRutbTb2uRY2Phkh"
url = "https://api.sarvam.ai/text-to-speech"

payload = {
    "text": "Hello world.",
    "target_language_code": "en-IN",
    "speaker": "meera",
    "model": "bulbul:v3"
}
headers = {
    "api-subscription-key": api_key,
    "Content-Type": "application/json"
}

print(f"Testing Sarvam API with model v3...")
try:
    response = requests.post(url, json=payload, headers=headers, timeout=20)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success!")
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Exception: {e}")

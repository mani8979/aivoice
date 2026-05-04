import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")

api_key = os.getenv("SARVAM_API_KEY")
# The REST API endpoint for Saravam TTS
url = "https://api.sarvam.ai/text-to-speech"

# Correct payload structure for Sarvam REST API
payload = {
    "text": "నమస్కారం, నేను ర్యాపిడ్ ఎక్స్ ఎస్టేట్స్ నుండి మాట్లాడుతున్నాను.",
    "target_language_code": "te-IN",
    "speaker": "anushka",
    "model": "bulbul:v2"
}
headers = {
    "api-subscription-key": api_key,
    "Content-Type": "application/json"
}

print(f"Testing Sarvam API with key: {api_key[:5]}...")
print(f"URL: {url}")
try:
    response = requests.post(url, json=payload, headers=headers, timeout=20)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success! Audio data received.")
        # print(f"Response length: {len(response.content)}")
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Exception: {e}")

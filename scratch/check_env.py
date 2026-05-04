import os
from dotenv import load_dotenv

load_dotenv(".env")

print(f"TTS_PROVIDER: {os.getenv('TTS_PROVIDER')}")
print(f"SARVAM_API_KEY: {os.getenv('SARVAM_API_KEY')[:10]}...")
print(f"LLM_PROVIDER: {os.getenv('LLM_PROVIDER')}")
print(f"STT_PROVIDER: {os.getenv('STT_PROVIDER')}")

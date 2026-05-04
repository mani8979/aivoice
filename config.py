import os
from dotenv import load_dotenv

load_dotenv()

# =========================================================================================
#  🤖 RAPID X AI - AGENT CONFIGURATION
#  Use this file to customize your agent's personality, models, and behavior.
# =========================================================================================

# --- 1. AGENT PERSONA & PROMPTS ---
# The main instructions for the AI. Defines who it is and how it behaves.
SYSTEM_PROMPT = """
CRITICAL RULE: You are EXCLUSIVELY a land sales assistant for "Rapid X Estates" in Vizag (Visakhapatnam).
You ONLY sell land in ONE location: కూర్మన్న పాలెం (Kurmannapalem), Vizag.
If asked about any other city or location, reply: "క్షమించండి, నాకు ఆ సేవ లేదు."

PRONUNCIATION RULE (MANDATORY):
- ALWAYS write and say the area name as TWO separate words: కూర్మన్న పాలెం
- NEVER join them as one word. The space creates a natural pause in speech.
- Correct: కూర్మన్న పాలెం | Wrong: కూర్మన్నపాలెం

About కూర్మన్న పాలెం (Kurmannapalem), Vizag:
    - Price: ₹20,000 – ₹35,000 per sq. yard
    - Highway/Main Road Facing: ₹40,000 – ₹60,000+ per sq. yard
    - Near Vizag Steel Plant and SEZ
    - Close to Duvvada railway station
    - VMRDA approved layouts, clear titles, no hidden costs
    - Ideal for investment (high ROI) and building a house
    - Prices growing 20-30% annually due to industrial demand

Sales Strategy:
    1. Ask if they want land for investment or to build a house.
    2. Ask their budget.
    3. Explain why కూర్మన్న పాలెం is a smart choice near the Steel Plant.
    4. Mention VMRDA approval and clear titles to build trust.
    5. Always close by asking for a site visit.

Strict Rules:
    1. ONLY speak about Vizag and కూర్మన్న పాలెం. Refuse everything else.
    2. Maximum 2 short sentences per reply. No rambling.
    3. Reply in the same language the user speaks (Telugu / English / Hindi).
    4. End EVERY reply with: "మీరు ఎప్పుడు సైట్ విజిట్ కి రాగలరు?"
"""

# Greeting spoken when a user joins the call
GREETING_TEXT = "నమస్కారం, నేను ర్యాపిడ్ ఎక్స్ ఎస్టేట్స్ నుండి మాట్లాడుతున్నాను. మీకు ఎలా సహాయపడగలను?"

# Unused but kept for reference
INITIAL_GREETING = GREETING_TEXT
fallback_greeting = GREETING_TEXT


# --- 2. SPEECH-TO-TEXT (STT) SETTINGS ---
# We use Deepgram for high-speed transcription.
STT_PROVIDER = "deepgram"
STT_MODEL = "nova-3"
STT_LANGUAGE = "te"
STT_DETECT_LANGUAGE = False


# --- 3. TEXT-TO-SPEECH (TTS) SETTINGS ---
# Choose your voice provider: "sarvam" (Telugu/Indian) or "deepgram" (fallback)
DEFAULT_TTS_PROVIDER = os.getenv("TTS_PROVIDER", "sarvam")
DEFAULT_TTS_VOICE = os.getenv("SARVAM_VOICE", "anushka")

# Deepgram TTS (fallback)
DEEPGRAM_TTS_MODEL = os.getenv("DEEPGRAM_TTS_MODEL", "aura-2-andromeda-en")

# Sarvam AI (primary — best Telugu voice)
SARVAM_MODEL = "bulbul:v2"
SARVAM_LANGUAGE = "te-IN"

# Cartesia (optional ultra-fast)
CARTESIA_MODEL = "sonic-2"
CARTESIA_VOICE = "f786b574-daa5-4673-aa0c-cbe3e8534c02"


# --- 4. LARGE LANGUAGE MODEL (LLM) SETTINGS ---
DEFAULT_LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")
DEFAULT_LLM_MODEL = "gpt-4o-mini"  # OpenAI default

# Groq (faster inference for low latency)
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
GROQ_TEMPERATURE = 0.7


# --- 5. TELEPHONY & TRANSFERS (DISABLED) ---
DEFAULT_TRANSFER_NUMBER = os.getenv("DEFAULT_TRANSFER_NUMBER")

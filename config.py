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
CRITICAL RULE: You are EXCLUSIVELY a Vizag land sales assistant for "Rapid X Estates". 
If the user asks about ANY topic other than Vizag real estate, land rates, or locations in Vizag (listed below), you MUST NOT provide any info. 
ONLY reply with: "క్షమించండి, నాకు ఆ సేవ లేదు." (Sorry, I do not have that service).

Core Objective: Build trust and drive site visits for Vizag land investments.

Sales Strategy (Efficiency First):
    1. Quick Qualify: Ask if they want land for investment (ROI) or for building a house. Ask for their budget early.
    2. Value Proposition: Highlight the Beach Corridor project, Bhogapuram Airport, and IT SEZ growth in Vizag.
    3. Scarcity & Growth: Mention that Vizag is the executive capital and prices are rising 20-30% annually.
    4. Trust: Emphasize VUDA/VMRDA approved layouts and clear titles.

Knowledge Base (Vizag Real Estate Hotspots):
    - Kurmannapalem (కూర్మన్నపాలెం): ₹20k – ₹35k/sq.yd. (Near Steel Plant, high industrial demand).
    - Madhurawada (మధురవాడ): ₹25k – ₹45k/sq.yd. (IT Hub, premium growth).
    - Bhogapuram (భోగాపురం): ₹15k – ₹30k/sq.yd. (New International Airport area - Best for long-term ROI).
    - Rushikonda (రుషికొండ): ₹50k – ₹1.2L/sq.yd. (Beach view, luxury, IT SEZ).
    - Gajuwaka (గాజువాక): ₹30k – ₹60k/sq.yd. (Commercial & Residential heart).
    - Kapuluppada (కాపులుప్పాడ): ₹20k – ₹35k/sq.yd. (Upcoming IT park, great investment).
    - Anandapuram (ఆనందపురం): ₹18k – ₹30k/sq.yd. (Intersection of 3 highways, strategic growth).
    - Pendurthi (పెందుర్తి): ₹15k – ₹25k/sq.yd. (Budget friendly, good connectivity).

Rules:
    1. Multilingual: Reply in the language the user uses (Telugu/English/Hindi).
    2. Conciseness: Keep replies to 1-2 short sentences. Do not ramble.
    3. Closing: Always try to end with: "మీరు ఎప్పుడు సైట్ విజిట్ కి రాగలరు?" (When can you come for a site visit?).
"""

# The explicit first message the agent speaks when the user picks up.
# This ensures the user knows who is calling immediately.
INITIAL_GREETING = "The user has picked up the call. Speak in fluent Telugu and say: నమస్కారం, నేను ర్యాపిడ్ ఎక్స్ ఎస్టేట్స్ నుండి మాట్లాడుతున్నాను. భూములు మరియు ప్లాట్ల గురించి మీకు సహాయం చేయడానికి మేము సిద్ధంగా ఉన్నాము. మీకు ఏ ప్రాంతంలో స్థలం కావాలి?"

# If the user initiates the call (inbound) or is already there:
fallback_greeting = "Speak in fluent Telugu and say: నమస్కారం, నేను ర్యాపిడ్ ఎక్స్ ఎస్టేట్స్ నుండి మాట్లాడుతున్నాను. భూములు మరియు ప్లాట్ల గురించి మీకు సహాయం చేయడానికి మేము సిద్ధంగా ఉన్నాము. మీకు ఏ ప్రాంతంలో స్థలం కావాలి?"

GREETING_TEXT = "నమస్కారం, నేను ర్యాపిడ్ ఎక్స్ ఎస్టేట్స్ నుండి మాట్లాడుతున్నాను. మీకు ఎలా సహాయపడగలను?"


# --- 2. SPEECH-TO-TEXT (STT) SETTINGS ---
# We use Deepgram for high-speed transcription.
STT_PROVIDER = "deepgram"
STT_MODEL = "nova-3"
STT_LANGUAGE = "te"
STT_DETECT_LANGUAGE = False


# --- 3. TEXT-TO-SPEECH (TTS) SETTINGS ---
# Choose your voice provider: "deepgram", "openai", "sarvam" (Indian voices), or "cartesia" (Ultra-fast)
DEFAULT_TTS_PROVIDER = os.getenv("TTS_PROVIDER", "sarvam") 
DEFAULT_TTS_VOICE = os.getenv("SARVAM_VOICE", "anushka")      # OpenAI: alloy, echo, shimmer | Sarvam: anushka, aravind

# Deepgram TTS
DEEPGRAM_TTS_MODEL = os.getenv("DEEPGRAM_TTS_MODEL", "aura-2-andromeda-en")

# Sarvam AI Specifics (for Indian Context)
SARVAM_MODEL = "bulbul:v2"
SARVAM_LANGUAGE = "te-IN"

# Cartesia Specifics
CARTESIA_MODEL = "sonic-2"
CARTESIA_VOICE = "f786b574-daa5-4673-aa0c-cbe3e8534c02"


# --- 4. LARGE LANGUAGE MODEL (LLM) SETTINGS ---
# Choose "openai" or "groq"
DEFAULT_LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")
DEFAULT_LLM_MODEL = "gpt-4o-mini" # OpenAI default

# Groq Specifics (Faster inference)
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
GROQ_TEMPERATURE = 0.7


# --- 5. TELEPHONY & TRANSFERS (DISABLED) ---
# Default number to transfer calls to if no specific destination is asked.
DEFAULT_TRANSFER_NUMBER = os.getenv("DEFAULT_TRANSFER_NUMBER")

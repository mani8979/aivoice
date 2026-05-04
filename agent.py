import os
import certifi

# Fix for macOS SSL Certificate errors - MUST be before other imports
os.environ['SSL_CERT_FILE'] = certifi.where()

import logging
import json
import asyncio
from dotenv import load_dotenv

from livekit import agents, api
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.agents.voice.agent_session import SessionConnectOptions
from livekit.agents.types import APIConnectOptions
from livekit.agents import tts as agents_tts
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
    sarvam,
)
from livekit.agents import llm

# Load environment variables
load_dotenv(".env")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("voice-agent")

import config

def _build_tts(config_provider: str = None, config_voice: str = None):
    """Configure TTS. Tries Sarvam first (for Telugu). Falls back to Deepgram on failure."""
    provider = (config_provider or os.getenv("TTS_PROVIDER", config.DEFAULT_TTS_PROVIDER)).lower()

    if config_voice in ["anushka", "aravind", "amartya", "dhruv"]:
        provider = "sarvam"

    if provider == "deepgram":
        model = os.getenv("DEEPGRAM_TTS_MODEL", config.DEEPGRAM_TTS_MODEL)
        logger.info(f"Using Deepgram TTS (Model: {model})")
        return deepgram.TTS(model=model)

    if provider == "sarvam":
        try:
            logger.info(f"Attempting Sarvam TTS (Voice: {config_voice or 'anushka'})")
            model = os.getenv("SARVAM_TTS_MODEL", config.SARVAM_MODEL)
            voice = config_voice or os.getenv("SARVAM_VOICE", "anushka")
            language = os.getenv("SARVAM_LANGUAGE", config.SARVAM_LANGUAGE)
            tts = sarvam.TTS(model=model, speaker=voice, target_language_code=language)
            # Force HTTP mode — Sarvam WebSocket times out in cloud environments.
            tts._capabilities = agents_tts.TTSCapabilities(streaming=False, aligned_transcript=False)
            tts.prewarm = lambda: None
            logger.info("Sarvam TTS configured successfully (HTTP mode).")
            return tts
        except Exception as e:
            logger.error(f"Sarvam TTS setup failed: {e}. Falling back to Deepgram TTS.")
            fallback_model = os.getenv("DEEPGRAM_TTS_MODEL", config.DEEPGRAM_TTS_MODEL)
            return deepgram.TTS(model=fallback_model)

    # Default to OpenAI
    logger.info(f"Using OpenAI TTS (Voice: {config_voice or 'alloy'})")
    model = os.getenv("OPENAI_TTS_MODEL", "tts-1")
    voice = config_voice or os.getenv("OPENAI_TTS_VOICE", config.DEFAULT_TTS_VOICE)
    return openai.TTS(model=model, voice=voice)


def _build_llm(config_provider: str = None):
    """Configure the LLM provider based on config or env vars."""
    provider = (config_provider or os.getenv("LLM_PROVIDER", config.DEFAULT_LLM_PROVIDER)).lower()

    if provider == "groq":
        logger.info("Using Groq LLM")
        return openai.LLM(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("GROQ_MODEL", config.GROQ_MODEL),
            temperature=float(os.getenv("GROQ_TEMPERATURE", str(config.GROQ_TEMPERATURE))),
        )
    
    # Default to OpenAI
    logger.info("Using OpenAI LLM")
    return openai.LLM(model=config.DEFAULT_LLM_MODEL)


@llm.function_tool(description="Get the current time in a specific city.")
def get_time(city: str) -> str:
    """Get the current time."""
    import datetime

    now = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time in {city} is {now}."

class VoiceAssistant(Agent):
    """
    A premium AI voice agent for web interaction.
    """
    def __init__(self, tools: list) -> None:
        super().__init__(
            instructions=config.SYSTEM_PROMPT,
            tools=tools
        )


async def entrypoint(ctx: agents.JobContext):
    """
    Main entrypoint for the AI Voice Agent.
    """
    logger.info(f"=== New job received for room: {ctx.room.name} ===")

    try:
        await ctx.connect()
        logger.info("Connected to LiveKit room successfully.")
    except Exception as e:
        logger.error(f"FATAL: Failed to connect to room: {e}")
        return

    # Initialize the Agent Session with plugins
    try:
        tts_instance = _build_tts()
        llm_instance = _build_llm()
        logger.info(f"TTS: {type(tts_instance).__name__} | LLM: {type(llm_instance).__name__}")

        session = AgentSession(
            vad=silero.VAD.load(),
            stt=deepgram.STT(
                model=config.STT_MODEL,
                language="te",
                detect_language=config.STT_DETECT_LANGUAGE,
            ),
            llm=llm_instance,
            tts=tts_instance,
            conn_options=SessionConnectOptions(
                tts_conn_options=APIConnectOptions(max_retry=3, retry_interval=2.0, timeout=45.0),
            ),
            min_endpointing_delay=0.3,  # Fast response — 300ms after user stops talking
            allow_interruptions=True,   # STOP speaking when user starts talking
        )
        logger.info("Agent session initialized successfully.")
    except Exception as e:
        logger.error(f"FATAL: Failed to initialize session: {e}")
        return

    # Start the session
    try:
        await session.start(
            room=ctx.room,
            agent=VoiceAssistant(tools=[get_time]),
            room_input_options=RoomInputOptions(
                audio_enabled=True,
                close_on_disconnect=True,
            ),
        )
        logger.info("Session started")
    except Exception as e:
        logger.error(f"Failed to start session: {e}")
        return

    logger.info("Agent is now active and listening (waiting for user to speak first).")


if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(
            entrypoint_fnc=entrypoint,
            agent_name="outbound-caller", 
        )
    )

import os
import asyncio
import sys
from livekit import api
from dotenv import load_dotenv

load_dotenv()

def to_livekit_api_url(url: str | None) -> str | None:
    if not url:
        return url
    return url.replace("wss://", "https://", 1).replace("ws://", "http://", 1)

async def create_rule():
    # Initialize the API client
    lk_api = api.LiveKitAPI(
        to_livekit_api_url(os.getenv("LIVEKIT_URL")),
        os.getenv("LIVEKIT_API_KEY"),
        os.getenv("LIVEKIT_API_SECRET"),
    )

    agent_name = os.getenv("LIVEKIT_AGENT_NAME", "outbound-caller")
    room_name = sys.argv[1] if len(sys.argv) > 1 else os.getenv("LIVEKIT_ROOM")

    if not room_name:
        print("Usage: python create_dispatch_rule.py <room-name>")
        print("The dashboard now creates this dispatch automatically for each new room.")
        return

    print(f"Dispatching '{agent_name}' to room '{room_name}'...")
    try:
        await lk_api.agent_dispatch.create_dispatch(
            api.CreateAgentDispatchRequest(
                agent_name=agent_name,
                room=room_name,
            )
        )
        print("Agent dispatch created successfully!")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure the Python agent is running and registered with the same agent name.")
    finally:
        # Try to close gracefully
        if hasattr(lk_api, 'aclose'):
            await lk_api.aclose()
        elif hasattr(lk_api, 'close'):
            await lk_api.close()

if __name__ == "__main__":
    asyncio.run(create_rule())

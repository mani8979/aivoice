import os
import asyncio
from livekit import api
from dotenv import load_dotenv

load_dotenv()

async def check():
    lk_api = api.LiveKitAPI(
        os.getenv("LIVEKIT_URL"),
        os.getenv("LIVEKIT_API_KEY"),
        os.getenv("LIVEKIT_API_SECRET"),
    )
    # Correct method to create a dispatch rule in 0.6.0+
    # It takes a CreateAgentDispatchRequest
    print("Classes in api:")
    print([m for m in dir(api) if 'CreateAgentDispatch' in m])
    
    await lk_api.aclose()

if __name__ == "__main__":
    asyncio.run(check())

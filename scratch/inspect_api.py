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
    print("Methods on lk_api.agent_dispatch:")
    print(dir(lk_api.agent_dispatch))
    await lk_api.aclose()

if __name__ == "__main__":
    asyncio.run(check())

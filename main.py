import asyncio
import os
import logging

# Fix for Python 3.10+ — must run before any pyrogram import
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyrogram import Client
from modules import load_all
from port import run_in_background

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

for var in ["API_ID", "API_HASH", "BOT_TOKEN"]:
    if not os.environ.get(var):
        raise EnvironmentError(f"Missing required env var: {var}")

app = Client(
    "/tmp/MediaToTelegraphLink",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN"],
)

load_all(app)
run_in_background()

if __name__ == "__main__":
    logger.info("Bot is starting...")
    app.run()
    logger.info("Bot stopped.")

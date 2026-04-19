# Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
# Main entry point — MediaToTelegraphLink bot

import os
import logging
from pyrogram import Client
from modules import load_all
from port import run_in_background

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

# ─── Bot client ──────────────────────────────────────────────────────────────
app = Client(
    "MediaToTelegraphLink",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN"],
)

# ─── Register all modules ────────────────────────────────────────────────────
load_all(app)

# ─── Start web server (required by Render) ───────────────────────────────────
run_in_background()

# ─── Run bot ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    logger.info("🤖 Bot is starting...")
    app.run()
    logger.info("🤖 Bot stopped.")

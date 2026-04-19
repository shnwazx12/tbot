# Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
# Module: Group chat /tl command → Telegraph link

import os
from pyrogram import filters
from pyrogram.types import Message
from telegraph import upload_file
from database import increment_upload

MEDIA_DIR = "./media/group/"


def register(app):

    @app.on_message(filters.command("tl"))
    async def get_link_group(client, message: Message):
        # Must be a reply to a media message
        if not message.reply_to_message or not message.reply_to_message.media:
            await message.reply("⚠️ Please use `/tl` as a **reply** to a valid media file.")
            return

        text = await message.reply("⏳ Processing...")

        async def progress(current, total):
            pct = current * 100 / total
            await text.edit_text(f"📥 Downloading... {pct:.1f}%")

        local_path = None
        try:
            os.makedirs(MEDIA_DIR, exist_ok=True)
            local_path = await message.reply_to_message.download(MEDIA_DIR, progress=progress)
            await text.edit_text("📤 Uploading to Telegraph...")
            upload_path = upload_file(local_path)
            telegraph_url = f"https://telegra.ph{upload_path[0]}"
            if message.from_user:
                increment_upload(message.from_user.id)
            await text.edit_text(
                f"**🌐 Telegraph Link:**\n\n`{telegraph_url}`"
            )
        except Exception as e:
            await text.edit_text(f"**❌ Upload failed**\n\n**Reason:** `{e}`")
        finally:
            if local_path and os.path.exists(local_path):
                os.remove(local_path)

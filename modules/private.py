# Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
# Module: Private chat media → Telegraph link

import os
from pyrogram import filters
from pyrogram.types import Message
from telegraph import upload_file
from database import add_user, increment_upload

MEDIA_DIR = "./media/private/"


def register(app):

    @app.on_message(filters.media & filters.private)
    async def get_link_private(client, message: Message):
        user = message.from_user
        add_user(user.id, user.username, user.full_name)

        text = await message.reply("⏳ Processing...")

        async def progress(current, total):
            pct = current * 100 / total
            await text.edit_text(f"📥 Downloading... {pct:.1f}%")

        local_path = None
        try:
            os.makedirs(MEDIA_DIR, exist_ok=True)
            local_path = await message.download(MEDIA_DIR, progress=progress)
            await text.edit_text("📤 Uploading to Telegraph...")
            upload_path = upload_file(local_path)
            telegraph_url = f"https://telegra.ph{upload_path[0]}"
            increment_upload(user.id)
            await text.edit_text(
                f"**🌐 Telegraph Link:**\n\n`{telegraph_url}`"
            )
        except Exception as e:
            await text.edit_text(f"**❌ Upload failed**\n\n**Reason:** `{e}`")
        finally:
            if local_path and os.path.exists(local_path):
                os.remove(local_path)

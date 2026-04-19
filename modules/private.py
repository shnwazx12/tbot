import os
from pyrogram import filters
from pyrogram.types import Message
from telegraph import upload_file
from database import add_user, increment_upload

MEDIA_DIR = "/tmp/media/private/"


def register(app):

    @app.on_message(filters.media & filters.private)
    async def get_link_private(client, message: Message):
        user = message.from_user
        add_user(user.id, user.username, user.full_name)

        text = await message.reply("⏳ Processing...")

        async def progress(current, total):
            await text.edit_text(f"📥 Downloading... {current * 100 / total:.1f}%")

        local_path = None
        try:
            os.makedirs(MEDIA_DIR, exist_ok=True)
            local_path = await message.download(MEDIA_DIR, progress=progress)
            await text.edit_text("📤 Uploading to Telegraph...")

            result = upload_file(local_path)

            # Handle all return types: list, dict, or raw string
            if isinstance(result, list):
                path = result[0]
            elif isinstance(result, dict):
                path = result.get("src") or result.get("path") or str(result)
            else:
                path = str(result)

            # Ensure it starts with /
            if not path.startswith("/"):
                path = "/" + path

            telegraph_url = f"https://telegra.ph{path}"
            increment_upload(user.id)
            await text.edit_text(f"**🌐 Telegraph Link:**\n\n`{telegraph_url}`")

        except Exception as e:
            await text.edit_text(f"**❌ Upload failed**\n\n**Reason:** `{e}`")
        finally:
            if local_path and os.path.exists(local_path):
                os.remove(local_path)

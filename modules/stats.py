from pyrogram import filters
from pyrogram.types import Message
from database import total_users, total_uploads, get_upload_count


def register(app):

    @app.on_message(filters.command("stats") & filters.private)
    async def stats(client, message: Message):
        text = (
            "**📊 Bot Statistics**\n\n"
            f"👤 Total Users: `{total_users()}`\n"
            f"📤 Total Uploads: `{total_uploads()}`\n"
            f"🗂️ Your Uploads: `{get_upload_count(message.from_user.id)}`"
        )
        await message.reply(text)

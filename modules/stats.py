# Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
# Module: Stats command

from pyrogram import filters
from pyrogram.types import Message
from database import total_users, total_uploads, get_upload_count


def register(app):

    @app.on_message(filters.command("stats") & filters.private)
    async def stats(client, message: Message):
        user_count = total_users()
        global_uploads = total_uploads()
        my_uploads = get_upload_count(message.from_user.id)

        text = (
            "**📊 Bot Statistics**\n\n"
            f"👤 Total Users: `{user_count}`\n"
            f"📤 Total Uploads: `{global_uploads}`\n"
            f"🗂️ Your Uploads: `{my_uploads}`"
        )
        await message.reply(text)

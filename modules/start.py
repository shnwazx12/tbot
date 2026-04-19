# Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
# Module: Start & Help commands

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user, total_users


def register(app):

    @app.on_message(filters.command("start") & filters.private)
    async def start(client, message: Message):
        user = message.from_user
        add_user(user.id, user.username, user.full_name)

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("📢 Channel", url="https://t.me/teletipsofficialchannel"),
                InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true"),
            ]
        ])

        text = (
            f"👋 Hey {user.mention},\n\n"
            "I generate **Telegraph links** for your media files.\n\n"
            "📎 **How to use:**\n"
            "• In **private chat** — just send any media file directly.\n"
            "• In **group chats** — reply to a media file with `/tl`.\n\n"
            "✅ Supported types: `jpeg`, `jpg`, `png`, `mp4`, `gif`\n\n"
            "🏠 | [Home](https://t.me/teletipsofficialchannel)"
        )
        await message.reply(text, reply_markup=keyboard, disable_web_page_preview=True)


    @app.on_message(filters.command("help") & filters.private)
    async def help_cmd(client, message: Message):
        text = (
            "**📖 Help Menu**\n\n"
            "`/start` — Welcome message\n"
            "`/help` — This message\n"
            "`/stats` — Your upload stats\n\n"
            "**Group Commands:**\n"
            "`/tl` — Reply to a media file to get a Telegraph link\n\n"
            "**Supported formats:** jpeg, jpg, png, mp4, gif"
        )
        await message.reply(text)

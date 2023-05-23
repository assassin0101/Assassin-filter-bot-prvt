import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
import os
from pyrogram import Client, filters
from dotenv import load_dotenv
load_dotenv()

from info import *


Bot = Client(
     os.environ.get("SESSION_NAME", "No-Forward-Messages"),
     api_id=API_ID,
     api_hash=API_HASH,
     bot_token=BOT_TOKEN
)

@Client.on_message(filters.forwarded & filters.group & filters.channel & filters.incoming)
async def channel_tag(bot, message):
    try:
        chat_id = message.chat.id
        forward_msg = await message.copy(chat_id)
        await message.delete()
    except:
        await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")


@Client.on_message(filters.forwarded & filters.group & filters.incoming)
async def forward(bot, message):
	await message.delete()

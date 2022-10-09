from multiprocessing.connection import Client
from pyrogram.types import Message
import pyrogram
from pyrogram import filters
from Shikimori import dispatcher
from telegram.ext import CallbackContext, CallbackQueryHandler
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update, InlineKeyboardMarkup, InlineKeyboardButton

from Shikimori import pbot as Client

@Client.on_message(filters.command(["anidl"]))
async def channelanisearch(update: Update, context: CallbackContext, client , message: Message):
    message = update.effective_message
    text1 = message.text[len('/anidl '):]
    async for message in Client.search_messages(chat_id=-1001787236718, query=text1, limit=120):
        message.reply_text(message.text)

CAS_HANDLER = DisableAbleCommandHandler(["anidl"], channelanisearch , run_async=True)

dispatcher.add_handler(CAS_HANDLER)

__command_list__ = ["anidl"]
__handlers__ = [CAS_HANDLER]

__mod_name__ = "Channel Anime Search"
__help__ = """
*Channel Anime Search"
 ❍ `/anidl` : Search for Anime in Anime Clan Index
 """
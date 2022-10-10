# from multiprocessing.connection import Client
# from pyrogram.types import Message
# import pyrogram
# from pyrogram import filters
# from Shikimori import dispatcher
# from telegram.ext import CallbackContext, CallbackQueryHandler
# from Shikimori.modules.disable import DisableAbleCommandHandler
# from telegram import ParseMode, Update, InlineKeyboardMarkup, InlineKeyboardButton

# from Shikimori import pbot as Client

# @Client.on_message(filters.command(["anidl"]))
# async def channelanisearch(update: Update, context: CallbackContext, client , message: Message):
#     message = update.effective_message
#     text1 = message.text[len('/anidl '):]
#     async for message in Client.search_messages(chat_id=-1001787236718, query=text1, limit=120):
#         message.reply_text(message.text)
#         print(message.text)

# CAS_HANDLER = DisableAbleCommandHandler(["anidl"], channelanisearch , run_async=True)

# dispatcher.add_handler(CAS_HANDLER)

# __command_list__ = ["anidl"]
# __handlers__ = [CAS_HANDLER]

# __mod_name__ = "Channel Anime Search"
# __help__ = """
# *Channel Anime Search"
#  ❍ `/anidl` : Search for Anime in Anime Clan Index
#  """

from urllib import request
from pyrogram import filters

from Shikimori import pbot as app, arq
from Shikimori.utils.errors import capture_err

import os
import json
import re
import requests

__mod_name__ = "Channel Anime Search"



@app.on_message(filters.command("anisearch"))
async def cas(_, message):
    if len(message.command) < 2:
        return await message.reply_text("/anisearch needs an argument")

    query = message.text.split(None, 1)[1]

    # word = input("Enter Anime name")

    capitalizedword = query.capitalize()

    # print(capitalizedword)

    wholequery = capitalizedword.split()

    # print(wholequery[0])
    print(os.getcwd())
    with open(r'animelinkstext.txt', 'r') as fp:
        # read all lines in a list
    # fp = requests.get("https://raw.githubusercontent.com/definitelynotchirag/AnimeTelegramLinks/main/README.md")
        # content = fp.read()
        lines = fp.readlines()


        for line in lines:
            if line.find(wholequery[0], re.IGNORECASE) != -1:
                # await message.reply_text("Searching")
                # await message.edit_text("Found The Anime")
            # print(query, 'string exists in file')
            # print('Line Number:', lines.index(line))
            # print('Line:', line)
                caption = f"""
                **Anime** {query}
                **Link** {line}            
                """
                await message.reply_text(caption)

            # print(line)

    # m = await message.reply_text("Searching")
    # reddit = await arq.reddit(subreddit)

    # async for message in app.search_messages(chat_id="Anime_Climax", query=query, limit=120):
    # print(message.text)
    # if not reddit.ok:
        # return await m.edit_text(message.text)
#     reddit = reddit.result
#     nsfw = reddit.nsfw
#     sreddit = reddit.subreddit
#     title = reddit.title
#     image = reddit.url
#     link = reddit.postLink
#     if nsfw:
#         return await m.edit_text("NSFW RESULTS COULD NOT BE SHOWN.")

#     caption = f"""
# **Title:** `{title}`
# **Subreddit:** {sreddit}
# **PostLink:** {link}"""
#     try:
#         await message.reply_photo(photo=image, caption=caption)
#         await m.delete()
#     except Exception as e:
#         await m.edit_text(e.MESSAGE)

__mod_name__ = "Channel Anime Search"
__help__ = """
*Channel Anime Search*
 ❍ `/anisearch` : Search for Anime in Anime Clan Index
"""
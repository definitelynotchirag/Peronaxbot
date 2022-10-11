#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : broadcast-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/broadcast-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

# import os
# import asyncio
# # from presets import Presets
# from pyrogram.types import Message
# from pyrogram import Client, filters
# from pyrogram.errors import FloodWait
# from Shikimori import pbot as app
# import Shikimori.modules.sql.users_sql as sql

# import asyncio
# import os
# import subprocess
# import time

# import psutil
# from pyrogram import filters
# from pyrogram.errors import FloodWait

# from library.support import users_info
# from library.sql import add_user, query_msg


# if bool(os.environ.get("ENV", False)):
#     from sample_config import Config
# else:
#     from config import Config


# # ------------------------------- Start Message --------------------------------- #
# @Client.on_message(filters.private & filters.command('start'))
# # async def start_bot(bot, m: Message):
# #     id = m.from_user.id
# #     user_name = '@' + m.from_user.username if m.from_user.username else None
# #     await add_user(id, user_name)
# #     await m.reply_text(Presets.WELCOME_MESSAGE.format(m.from_user.mention(),
# #                                                       Config.SUPPORT_CHAT if Config.SUPPORT_CHAT else "_______"),
# #                        parse_mode='html',
# #                        disable_web_page_preview=True
# #                        )


# # ------------------------------- View Subscribers --------------------------------- #
# @Client.on_message(filters.private & filters.command('subscribers'))
# async def subscribers_count(bot, m: Message):
#     id = m.from_user.id
#     if id not in Config.AUTH_USERS:
#         return
#     msg = await m.reply_text(Presets.WAIT_MSG)
#     messages = await users_info(bot)
#     active = messages[0]
#     blocked = messages[1]
#     await m.delete()
#     await msg.edit(Presets.USERS_LIST.format(active, blocked))


# # ------------------------ Send messages to subs ----------------------------- #
# @Client.on_message(filters.private & filters.command('send'))
# async def send_text(bot, m: Message):
#     id = m.from_user.id
#     if id not in Config.AUTH_USERS:
#         return
#     if (" " not in m.text) and ("send" in m.text) and (m.reply_to_message is not None):
#         query = await query_msg()
#         for row in query:
#             chat_id = int(row[0])
#             try:
#                 await bot.copy_message(
#                     chat_id=chat_id,
#                     from_chat_id=m.chat.id,
#                     message_id=m.reply_to_message.message_id,
#                     caption=m.reply_to_message.caption,
#                     reply_markup=m.reply_to_message.reply_markup
#                 )
#             except FloodWait as e:
#                 await asyncio.sleep(e.x)
#             except Exception:
#                 pass
#     else:
#         msg = await m.reply_text(Presets.REPLY_ERROR, m.message_id)
#         await asyncio.sleep(8)
#         await msg.delete()


# __mod_name__ = "Broadcast"
# __help__ = """
# *Broadcast*
#  ❍ `/send` : Broadcast to all users
# """

# chatsdb = chats = sql.get_all_chats() or []

# async def get_served_chats() -> list:
#     chats_list = []
#     async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
#         chats_list.append(chat)
#     return chats_list


# @app.on_message(filters.command("broadcast") & SUDOERS & ~filters.edited)
# # @capture_err
# async def broadcast_message(_, message):
#     if len(message.command) < 2:
#         return await message.reply_text("**Usage**:\n/broadcast [MESSAGE]")
#     sleep_time = 0.1
#     text = message.text.split(None, 1)[1]
#     sent = 0
#     schats = await get_served_chats()
#     chats = [int(chat["chat_id"]) for chat in schats]
#     m = await message.reply_text(
#         f"Broadcast in progress, will take {len(chats) * sleep_time} seconds."
#     )
#     for i in chats:
#         try:
#             await app.send_message(i, text=text)
#             await asyncio.sleep(sleep_time)
#             sent += 1
#         except FloodWait as e:
#             await asyncio.sleep(int(e.x))
#         except Exception:
#             pass
#     await m.edit(f"**Broadcasted Message In {sent} Chats.**")
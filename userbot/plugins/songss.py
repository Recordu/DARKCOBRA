# plugin made by @hellboi_atul
# Copyright (C) DARK COBRA 2020.

from telethon import events
import asyncio
#from userbot.utils import admin_cmd
from userbot.events import register 
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os
try:
 import subprocess
except:
 os.system("pip install instantmusic")



os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s "+name)



@register(outgoing=True, pattern="^.gaana(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@FindMusicPleaseBot"
    await event.edit("```Getting Your Music Ser```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`Downloading, Stay Tuned.....`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=442186886))
              await bot.send_message(chat, link)
              respond = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @FindMusicPleaseBot and try again```")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)
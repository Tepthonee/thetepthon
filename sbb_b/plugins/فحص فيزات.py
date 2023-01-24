""" 
CC Visa @Tepthon

"""

import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from sbb_b import sbb_b

from ..core.managers import edit_or_reply


@sbb_b.ar_cmd(pattern="cc(?:\s|$)([\s\S]*)")
async def song2(event):
    card = event.pattern_match.group(1)
    chat = "@SDBB_Bot"
    reply_id_ = await reply_id(event)
    tep = await edit_or_reply(event, "**- جاري فحص الـبطــاقـة انـتـظـر قلـيلًا 🧸♥️ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await sbb_b(unblock("SDBB_Bot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await tep.delete()


@sbb_b.ar_cmd(pattern="فيزا(?:\s|$)([\s\S]*)")
async def song2(event):
    chat = "@SDBB_Bot"
    reply_id_ = await reply_id(event)
    tep = await edit_or_reply(event, "**- جـارِ تولـيد بن 𝚅𝙸𝚂𝙴💲...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/gen 547292000038xxxx|RND|RND|RND")
        except YouBlockedUserError:
            await sbb_b(unblock("SDBB_Bot"))
            await conv.send_message("/gen 547292000038xxxx|RND|RND|RND")
        await asyncio.sleep(2)
        response = await conv.get_response()
        if response.text.startswith("البطاقه ⇽"):
        	return await tep.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await tep.delete()


@sbb_b.ar_cmd(pattern="توليد(?:\s|$)([\s\S]*)")
async def song2(event):
    been = event.pattern_match.group(1)
    chat = "@SDBB_Bot"
    reply_id_ = await reply_id(event)
    tep = await edit_or_reply(event, f"**- جـارِ توليـد 10 بطاقـات ع الـ Bin {been}  💳...**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "توليد {}".format(been)
            await conv.send_message("/setbin")
            await asyncio.sleep(2)
            await conv.send_message(gool)
            await asyncio.sleep(2)
            await conv.send_message("/combo")
        except YouBlockedUserError:
            await sbb_b(unblock("SDBB_Bot"))
            gool = "توليد {}".format(been)
            await conv.send_message("/setbin")
            await asyncio.sleep(2)
            await conv.send_message(gool)
            await asyncio.sleep(2)
            await conv.send_message("/combo")
        await asyncio.sleep(7)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await tep.delete()


@sbb_b.ar_cmd(pattern="ماستر(?:\s|$)([\s\S]*)")
async def song2(event):
    card = event.pattern_match.group(1)
    chat = "@SDBB_Bot"
    reply_id_ = await reply_id(event)
    tep = await edit_or_reply(event, "**- جـارِ تولـيد بن 𝙼𝙰𝚂𝚃𝙴𝚁𝙲𝙰𝚁𝙳 💳...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("ماستر")
        except YouBlockedUserError:
            await sbb_b(unblock("SDBB_Bot"))
            await conv.send_message("ماستر")
        await asyncio.sleep(2)
        response = await conv.get_response()
        if response.text.startswith("البطاقه ⇽"):
        	return await tep.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await tep.delete()


@sbb_b.ar_cmd(pattern="اماكس(?:\s|$)([\s\S]*)")
async def song2(event):
    card = event.pattern_match.group(1)
    chat = "@SDBB_Bot"
    reply_id_ = await reply_id(event)
    tep = await edit_or_reply(event, "**- جـارِ تولـيد بن 🇧🇷 𝙰𝙼𝙴𝚇...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(event)
        except YouBlockedUserError:
            await sbb_b(unblock("SDBB_Bot"))
            await conv.send_message(event)
        await asyncio.sleep(2)
        response = await conv.get_response()
        if response.text.startswith("البطاقه ⇽"):
        	return await tep.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await tep.delete()

#كتابة_وتعديل_حمد
#hmd.txt

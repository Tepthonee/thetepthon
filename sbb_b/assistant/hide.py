import json
import os
import re

from telethon.events import CallbackQuery

from sbb_b import sbb_b


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(b"hide_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./sbb_b/hide.txt"):
        jsondata = json.load(open("./sbb_b/hide.txt"))
        try:
            reply_pop_up_alert = jsondata[f"{timestamp}"]["text"]
        except KeyError:
            reply_pop_up_alert = "هذه الرسالة غير متوفرة الان في سيرفرات جمثون"
    else:
        reply_pop_up_alert = "هذه الرسالة غير متوفرة"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

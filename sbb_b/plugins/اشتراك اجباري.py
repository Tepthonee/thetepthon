import requests
from telethon import Button
from telethon.tl.functions.messages import ExportChatInviteRequest

from sbb_b import BOTLOG_CHATID, sbb_b

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus


#اشهد ان لا اله الا الله واشهد أن محمدًا عبده ورسوله 
# اخ اخ اخ اخ اخ اخ اخممممممط ياطويل العمر اخمطط 😂
# Tepthon - file - official
@sbb_b.ar_cmd(pattern="اشتراك")
async def reda(event):
    ty = event.text
    ty = ty.replace(".اشتراك", "")
    ty = ty.replace(" ", "")
    if len(ty) < 2:
        return await edit_delete(
            event, "**✤︙ قم بكتابة نوع الاشتراك الاجباري كروب او خاص 🤔**"
        )
    if ty == "كروب":
        if not event.is_group:
            return await edit_delete(
                "**✤︙ استعمل الأمر في الجروب المراد تفعيل الاشتراك الاجباري به**"
            )
        if event.is_group:
            if gvarstatus("subgroup") == event.chat_id:
                return await edit_delete(
                    event, "**✤︙ الاشتراك الاجباري مفعل لهذا الكروب**"
                )
            if gvarstatus("subgroup"):
                return await edit_or_reply(
                    event,
                    "**✤︙ الاشتراك الاجباري مفعل لكروب اخر قم بالغائه لتفعيله في كروب اخر**",
                )
            addgvar("subgroup", f"{event.chat_id}")
            return await edit_or_reply(
                event, "**✤︙ تم تفعيل الاشتراك الاجباري لهذه المجموعة ✓**"
            )
    if ty == "خاص":
        if gvarstatus("subprivate"):
            return await edit_delete(
                event, "**✤︙ الاشتراك الاجباري للخاص مُفعل بالفعل ✓**"
            )
        if not gvarstatus("subprivate"):
            addgvar("subprivate", True)
            await edit_or_reply(event, "**✤︙ تم تفعيل الاشتراك الاجباري للخاص ✓**")
    if ty not in ["خاص", "كروب"]:
        return await edit_delete(
            event, "**✤︙ قم بكتابة نوع الاشتراك الاجباري خاص او كروب 🤔**"
        )


@sbb_b.ar_cmd(pattern="تعطيل")
async def reda(event):
    cc = event.text.replace(".تعطيل", "")
    cc = cc.replace(" ", "")
    if len(cc) < 2:
        return await edit_delete(
            event, "**✤︙ قم بكتابة نوع الاشتراك الاجباري لإلغائه**"
        )
    if cc == "كروب":
        if not gvarstatus("subgroup"):
            return await edit_delete("**✤︙ لم تفعل الاشتراك الاجباري للكروب لإلغائه**")
        if gvarstatus("subgroup"):
            delgvar("subgroup")
            return await edit_delete(
                event, "**✤︙ تم الغاء الاشتراك الاجباري للكروب بنجاح ✓**"
            )
    if cc == "خاص":
        if not gvarstatus("subprivate"):
            return await edit_delete(
                event, "**✤︙ الاشتراك الاجباري للخاص غير مفعل لإلغائه**"
            )
        if gvarstatus("subprivate"):
            delgvar("subprivate")
            return await edit_delete(event, "**✤︙ تم إلغاء الاشتراك الاجباري للخاص ✓**")
    if cc not in ["خاص", "كروب"]:
        return await edit_delete(
            event, "**✤︙ قم بكتابة نوع الاشتراك الاجباري لإلغائه ✓**"
        )


@sbb_b.ar_cmd(incoming=True)
async def reda(event):
    if gvarstatus("subprivate"):
        if event.is_private:
            try:

                idd = event.peer_id.user_id
                tok = Config.TG_BOT_TOKEN
                ch = gvarstatus("pchan")
                if not ch:
                    return await sbb_b.tgbot.send_message(
                        BOTLOG_CHATID,
                        "** انت لم تضع قناة الاشتراك الاجباري قم بوضعها**",
                    )
                try:
                    ch = int(ch)
                except BaseException as r:
                    return await sbb_b.tgbot.send_message(
                        BOTLOG_CHATID, f"**حدث خطأ \n{r}**"
                    )
                url = f"https://api.telegram.org/bot{tok}/getchatmember?chat_id={ch}&user_id={idd}"
                req = requests.get(url)
                reqt = req.text
                if "chat not found" in reqt:
                    mb = await sbb_b.tgbot.get_me()
                    mb = mb.username
                    await sbb_b.tgbot.send_message(
                        BOTLOG_CHATID,
                        f"**البوت الخاص بك @{mb} ليس في قناة الاشتراك الاجباري**",
                    )
                    return
                if "bot was kicked" in reqt:
                    mb = await sbb_b.tgbot.get_me()
                    mb = mb.username
                    await sbb_b.tgbot.send_message(
                        BOTLOG_CHATID,
                        "** البوت الخاص بك @{mb} مطرود من قناة الاشتراك الاجباري اعد اضافته**",
                    )
                    return
                if "not found" in reqt:
                    try:
                        c = await sbb_b.get_entity(ch)
                        chn = c.username
                        if c.username == None:
                            ra = await sbb_b.tgbot(ExportChatInviteRequest(ch))
                            chn = ra.link
                        if chn.startswith("https://"):
                            await event.reply(
                                f"**✤︙ يجب عليك ان تشترك بالقناة أولاً\nقناة الاشتراك : {chn}**",
                                buttons=[(Button.url("اضغط هنا", chn),)],
                            )
                            return await event.delete()
                        else:
                            await event.reply(
                                f"**✤︙ للتحدث معي يجب عليك الاشتراك في القناة\n قناة الاشتراك : @{chn} **",
                                buttons=[
                                    (Button.url("اضغط هنا", f"https://t.me/{chn}"),)
                                ],
                            )
                            return await event.delete()
                    except BaseException as er:
                        await sbb_b.tgbot.send_message(BOTLOG_CHATID, f"حدث خطا \n{er}")
                if "left" in reqt:
                    try:
                        c = await sbb_b.get_entity(ch)
                        chn = c.username
                        if c.username == None:
                            ra = await sbb_b.tgbot(ExportChatInviteRequest(ch))
                            chn = ra.link
                        if chn.startswith("https://"):
                            await event.reply(
                                f"**✤︙ يجب عليك ان تشترك بالقناة أولاً\nقناة الاشتراك : {chn}**",
                                buttons=[(Button.url("اضغط هنا", chn),)],
                            )
                            return await event.message.delete()
                        else:
                            await event.reply(
                                f"**✤︙ للتحدث معي يجب عليك الاشتراك في القناة\n قناة الاشتراك : @{chn} **",
                                buttons=[
                                    (Button.url("اضغط هنا", f"https://t.me/{chn}"),)
                                ],
                            )
                            return await event.message.delete()
                    except BaseException as er:
                        await sbb_b.tgbot.send_message(BOTLOG_CHATID, f"حدث خطا \n{er}")
                if "error_code" in reqt:
                    await sbb_b.tgbot.send_message(
                        BOTLOG_CHATID,
                        f"**حدث خطأ غير معروف قم باعادة توجيه الرسالة ل@ZQ_lO لحل المشكلة\n{reqt}**",
                    )

                return
            except BaseException as er:
                await sbb_b.tgbot.send_message(BOTLOG_CHATID, f"** حدث خطا\n{er}**")

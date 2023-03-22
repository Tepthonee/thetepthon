#بسم الله الرحمن الرحيم
from telethon import events
from sbb_b import sbb_b
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete
from telethon import functions
from telethon.errors.rpcerrorlist import MessageIdInvalidError
@sbb_b.on(admin_cmd(pattern="(خط الغامق|خط غامق)"))
async def btext(event):
    isbold = gvarstatus("bold")
    if not isbold:
        addgvar ("bold", "on")
        await edit_delete(event, "**تم تفعيل الخط الغامق بنجاح الآن**")
        return

    if isbold:
        delgvar("bold")
        await edit_delete(event, "**تم إطفاء الخط الغامق بنجاح الآن **")
        return

@sbb_b.on(admin_cmd(pattern="(خط رمز|خط الرمز)"))
async def btext(event):
    isramz = gvarstatus("ramz")
    if not isramz:
        addgvar ("ramz", "on")
        await edit_delete(event, "**تم تفعيل خط الرمز بنجاح الآن**")
        return

    if isramz:
        delgvar("ramz")
        await edit_delete(event, "**تم اطفاء خط الرمز بنجاح الآن **")
        return

@sbb_b.on(events.NewMessage(outgoing=True))
async def reda(event):
    isbold = gvarstatus("bold")
    if isbold:
        try:
            await event.edit(f"**{event.message.message}**")
        except MessageIdInvalidError:
            pass
    isramz = gvarstatus("ramz")
    if isramz:
        try:
            await event.edit(f"`{event.message.message}`")
        except MessageIdInvalidError:
            pass

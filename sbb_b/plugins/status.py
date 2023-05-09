import os
import urllib

from telethon.tl import functions
from sbb_b import sbb_b
from sbb_b.core.managers import edit_delete, edit_or_reply
from sbb_b.sql_helper.globals import addgvar, gvarstatus

plugin_category = "utils"


OFFLINE_TAG = "اوفلاين"


@sbb_b.ar_cmd(
    pattern="اوفلاين$",
    command=("اوفلاين", plugin_category),
    info={
        "header": "To your status as offline",
        "description": " it change your pic as offline, and add offline tag in name.",
        "usage": "{tr}offline",
    },
)
async def pussy(event):
    "make yourself offline"
    user = await event.client.get_entity("me")
    if user.first_name.startswith(OFFLINE_TAG):
        return await edit_delete(event, "**أنت مفعل الوضع بالفعل.**")
    await edit_or_reply(event, "**جاري تغير الحساب ل اوفلاين.**")
    photo = "./temp/donottouch.jpg"
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    urllib.request.urlretrieve(
        "https://graph.org/file/bccf7f1699a0d3e979601.jpg", photo
    )
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await edit_or_reply(event, str(e))
        else:
            await edit_or_reply(event, "**أنت الآن اوفلاين**")
    os.remove(photo)
    first_name = user.first_name
    addgvar("my_first_name", first_name)
    addgvar("my_last_name", "")
    if last_name := user.last_name:
        addgvar("my_last_name", last_name)
    tag_name = OFFLINE_TAG
    await event.client(
        functions.account.UpdateProfileRequest(
            last_name=first_name, first_name=tag_name
        )
    )
    await edit_delete(event, f"**`{tag_name} {first_name}`\nأنا مغلق الوقتي.**")


@sbb_b.ar_cmd(
    pattern="اونلاين$",
    command=("اونلاين", plugin_category),
    info={
        "header": "To your status as online",
        "description": " it change your pic back normal, and remove offline tag in name.",
        "usage": "{tr}online",
    },
)
async def cat(event):
    "make yourself online"
    user = await event.client.get_entity("me")
    if user.first_name.startswith(OFFLINE_TAG):
        await edit_or_reply(event, "**جاري إعادة الحساب مثل ما كان سابقًا...**")
    else:
        await edit_delete(event, "**أنت اونلاين بالفعل.**")
        return
    try:
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await edit_or_reply(event, str(e))
    else:
        await edit_or_reply(event, "**جاري إعادة الحساب مثل ما كان سابقًا....**")
    first_name = gvarstatus("my_first_name")
    last_name = gvarstatus("my_last_name") or ""
    await event.client(
        functions.account.UpdateProfileRequest(
            last_name=last_name, first_name=first_name
        )
    )
    await edit_delete(event, f"**`{first_name} {last_name}`\nأنا اونلاين !**")

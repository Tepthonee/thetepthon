#كتابة_حمد
#ترجمة_و_تعريب_فريق_تيبثون
from geopy.geocoders import Nominatim
from telethon.tl import types

from sbb_b import sbb_b

from ..core.managers import edit_or_reply
from ..helpers import reply_id

plugin_category = "extra"


@sbb_b.ar_cmd(
    pattern="جي بس اس ([\s\S]*)",
    command=("gps", plugin_category),
    info={
        "header": "To send the map of the given location.",
        "usage": "{tr}gps <place>",
        "examples": "{tr}gps Hyderabad",
    },
)
async def gps(event):
    "✥ : خريطة الموقع المحدد"
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, "`✥ : العثور على.....`")
    geolocator = Nominatim(user_agent="tepthon")
    if geoloc := geolocator.geocode(input_str):
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.client.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            caption=f"**الموقع ✥ : **`{input_str}`",
            reply_to=reply_to_id,
        )
        await catevent.delete()
    else:
        await catevent.edit("`✥ : لم أتمكن من العثور عليه`")

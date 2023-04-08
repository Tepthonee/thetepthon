#Semo_by_hmd
import re

from sbb_b import sbb_b 

IF_EMOJI = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    return re.sub(IF_EMOJI, "", inputString)


@sbb_b.ar_cmd(pattern="شطرنج(?: |$)(.*)")
async def nope(event):
    ok = event.pattern_match.group(1)
    if not ok:
        if event.is_reply:
            (await event.get_reply_message()).message

            return
    xoxoxo = await bot.inline_query("chessy_bot", f"{(deEmojify(ok))}")
    await xoxoxo[0].click(
        event.chat_id,
        reply_to=event.reply_to_msg_id,
        silent=True if event.is_reply else False,
        hide_via=True,
    )
    await event.delete()

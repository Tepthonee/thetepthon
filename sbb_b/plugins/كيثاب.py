import os
from datetime import datetime

import aiohttp
import requests
from github import Github
from pySmartDL import SmartDL

from sbb_b import sbb_b

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import reply_id

LOGS = logging.getLogger(os.path.basename(__name__))
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
plugin_category = "misc"

GIT_TEMP_DIR = "./temp/"


@sbb_b.ar_cmd(
    pattern="تيبثون$",
    command=("repo", plugin_category),
    info={
        "header": "Source code link of sbb_b",
        "usage": [
            "{tr}repo",
        ],
    },
)
async def source(e):
    "سورس تيبثون"
    await edit_or_reply(
        e,
        "اضغط [هنا](t.me/Tepthon) لفتح قناة السورس\
        \nاضغط [هنا](t.me/Tepthon_Help) كروب الدعم",
    )


@sbb_b.ar_cmd(
    pattern="كيثهاب( -l(\d+))? ([\s\S]*)",
    command=("github", plugin_category),
    info={
        "header": "Shows the information about an user on GitHub of given username",
        "flags": {"-l": "repo limit : default to 5"},
        "usage": ".github [flag] [username]",
        "examples": [".github sandy1709", ".github -l5 sandy1709"],
    },
)
async def _(event):
    "Get info about an GitHub User"
    reply_to = await reply_id(event)
    username = event.pattern_match.group(3)
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await edit_delete(event, f"`{username} not found`")
            catevent = await edit_or_reply(event, "`fetching github info ...`")
            result = await request.json()
            photo = result["avatar_url"]
            if result["bio"]:
                result["bio"] = result["bio"].strip()
            repos = []
            sec_res = requests.get(result["repos_url"])
            if sec_res.status_code == 200:
                limit = event.pattern_match.group(2)
                limit = int(limit) if limit else 5
                for repo in sec_res.json():
                    repos.append(f"[{repo['name']}]({repo['html_url']})")
                    limit -= 1
                    if limit == 0:
                        break
            REPLY = "**✥ : معلومات الكيثهاب من** `{username}`\
                \n👤 **✥ الاسم:** [{name}]({html_url})\
                \n🔧 **✥ النوع:** `{type}`\
                \n🏢 **✥ الشركة:** `{company}`\
                \n🔭 **✥ المدونة** : {blog}\
                \n📍 **✥ الموقع** : `{location}`\
                \n📝 **✥ النبذة** : __{bio}__\
                \n❤️ **✥ المتابعون** : `{followers}`\
                \n👁 **✥ الذين يتابعهم** : `{following}`\
                \n📊 **✥ الريبوات العامة** : `{public_repos}`\
                \n📄 **✥ الجماهير العامة** : `{public_gists}`\
                \n🔗 **✥ تم إنشاء الملف الشخصي** : `{created_at}`\
                \n✏️ **✥ تم تحديث الملف الشخصي** : `{updated_at}`".format(
                username=username, **result
            )

            if repos:
                REPLY += "\n🔍 **✥ بعض الريبوات** : " + " | ".join(repos)
            downloader = SmartDL(photo, ppath, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
            await event.client.send_file(
                event.chat_id,
                ppath,
                caption=REPLY,
                reply_to=reply_to,
            )
            os.remove(ppath)
            await catevent.delete()


@sbb_b.ar_cmd(
    pattern="ارتكب$",
    command=("commit", plugin_category),
    info={
        "header": "To commit the replied plugin to github.",
        "description": "It uploads the given file to your github repo in **sbb_b/plugins** folder\
        \nTo work commit plugin set `GITHUB_ACCESS_TOKEN` and `GIT_REPO_NAME` Variables in Heroku vars First",
        "note": "As of now not needed i will sure develop it ",
        "usage": "{tr}commit",
    },
)
async def download(event):
    "لربط البرنامج المساعد الذي تم الرد عليه في جيثب."
    if Config.GITHUB_ACCESS_TOKEN is None:
        return await edit_delete(
            event, "`يرجى إضافة رمز الوصول المناسب من github.com`", 5
        )
    if Config.GIT_REPO_NAME is None:
        return await edit_delete(
            event, "`الرجاء إضافة اسم Github Repo الصحيح لبرنامج المستخدم الخاص بك`", 5
        )
    mone = await edit_or_reply(event, "`✥ : جــاري الــمـعــالــجــة ...`")
    if not os.path.isdir(GIT_TEMP_DIR):
        os.makedirs(GIT_TEMP_DIR)
    start = datetime.now()
    reply_message = await event.get_reply_message()
    if not reply_message or not reply_message.media:
        return await edit_delete(
            event, "__Reply to a file which you want to commit in your github.__"
        )
    try:
        downloaded_file_name = await event.client.download_media(reply_message.media)
    except Exception as e:
        await mone.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await mone.edit(f"تم التنزيل إلى ✥ `{downloaded_file_name}` in {ms} seconds.")
        await mone.edit("الالتزام بجيثب....")
        await git_commit(downloaded_file_name, mone)


async def git_commit(file_name, mone):
    content_list = []
    access_token = Config.GITHUB_ACCESS_TOKEN
    g = Github(access_token)
    file = open(file_name, "r", encoding="utf-8")
    commit_data = file.read()
    repo = g.get_repo(Config.GIT_REPO_NAME)
    LOGS.info(repo.name)
    create_file = True
    contents = repo.get_contents("")
    for content_file in contents:
        content_list.append(str(content_file))
        LOGS.info(content_file)
    for i in content_list:
        create_file = True
        if i == 'ContentFile(path="' + file_name + '")':
            return await mone.edit("`File Already Exists`")
    if create_file:
        file_name = f"sbb_b/plugins/{file_name}"
        LOGS.info(file_name)
        try:
            repo.create_file(
                file_name, "Uploaded New Plugin", commit_data, branch="master"
            )
            LOGS.info("Committed File")
            ccess = Config.GIT_REPO_NAME
            ccess = ccess.strip()
            await mone.edit(
                f"`Commited On Your Github Repo`\n\n[Your PLUGINS](https://github.com/{ccess}/tree/master/sbb_b/plugins/)"
            )
        except BaseException:
            LOGS.info("Cannot Create Plugin")
            await mone.edit("Cannot Upload Plugin")
    else:
        return await mone.edit("`Committed Suicide`")

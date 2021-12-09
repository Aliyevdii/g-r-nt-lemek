# (c) 2021-22 < @xditya >
# < @BotzHub >

import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# start the bot
print("Başlanır...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    FRWD_CHANNEL = config("FRWD_CHANNEL", cast=int)
    BotzHub = TelegramClient('BotzHub', apiid, apihash).start(bot_token=bottoken)
except:
    print("Ətraf mühitin xüsusiyyətləri yoxdur! Zəhmət olmasa, yenidən yoxlayın.")
    print("Bot tərk edir...")
    exit()

@BotzHub.on(events.NewMessage(pattern="/start", func=lambda e: e.is_private))
async def _(event):
    ok = await BotzHub(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hello {ok.user.first_name}! \nI'm a Baxış sayğacı botu.\nənə mesaj göndər və mən'ona baxış sayı əlavə edəcək!",
                    buttons=[
                        [Button.url("Dev.", url="https://t.me/BotzHub"),
                        Button.url("Repository", url="https://github.com/Aliyevdii/g-r-nt-lemek")]
                    ])

@BotzHub.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def countit(event):
    if event.text.startswith('/'):
        return
    x = await event.forward_to(FRWD_CHANNEL)
    await x.forward_to(event.chat_id)

print("Bot has started.")
print("Do visit @BotzHub..")
BotzHub.run_until_disconnected()

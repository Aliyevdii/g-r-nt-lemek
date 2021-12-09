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
    ok = await NEXUS_MMC(GetFullUserRequest(event.sender_id))
    await event.reply(f"Salam {ok.user.first_name}! \nBu Bot Kanalara Ekləyərək Görüntüləmə Sayısını Artıra Bilərsiniz!",
                    buttons=[
                        [Button.url("𝐎𝐰𝐧𝐞𝐫.", url="https://t.me/A_l_i_y_e_v_d_i"),
                        Button.url("𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/NEXUS_MMC")]
                    ])

@BotzHub.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def countit(event):
    if event.text.startswith('/'):
        return
    x = await event.forward_to(FRWD_CHANNEL)
    await x.forward_to(event.chat_id)

print("Bot başladı.")
print("Ziyarət edin @iron_Blood_Gurup..")
NEXUS_MMC.run_until_disconnected()

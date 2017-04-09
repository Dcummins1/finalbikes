import requests
import json

APIKEY = "58c66e96f312aedb78f7f726e5da74ec7ade7e33"
NAME = "Dublin"
STATIONS_URI = "https://api.jcdecaux.com/vls/v1/stations"
r = requests.get(STATIONS_URI, params={"apiKey": APIKEY,
 "contract": NAME})

a = json.dumps(json.JSONDecoder().decode(r.text))
print(a)

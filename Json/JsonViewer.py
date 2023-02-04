import requests
import json


# LINK = ("http://api.weatherapi.com/v1/future.json?key=df8a79d600db4388880121515232301&q=astana&dt=2023-03-03")
LINK = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
# LINK =
# LINK =

resp = requests.get(LINK)
json_like = json.dumps(resp.json(), indent=2)
# print(json_like)

# write to json_temp.json file
with open('json_temp.json', 'w') as file:
    file.write(json_like)

x = resp.json()[357]['kp_index']

print(x)

# /357/kp_index
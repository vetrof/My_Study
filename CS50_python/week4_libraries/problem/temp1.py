import requests
import json

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
json_file = response.json()

# for dict in json_file:

    # print(json_file[dict])

print(json_file['bpi']['USD']['rate'])

# /bpi/USD/rate




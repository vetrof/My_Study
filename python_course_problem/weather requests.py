import requests
from pprint import pprint
API_Key = '1277f2a3cb8b7642fe6f9411b4f08a8d'

#location = input("Enter Your Desired Location: ")
location = 'saint petersburg'
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()
pprint(weather_data)
print()

#print(weather_data)


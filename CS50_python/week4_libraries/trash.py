import requests
import sys

search = sys.argv[1]

resp = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term=' + search)
file = resp.json()
# print(json.dumps(resp.json(), indent=2))
for result in file['results']:
    print(result['trackName'])

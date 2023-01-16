# Harvard / cs50p / python
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

import requests
import sys

# search = sys.argv[1]
search = 'acdc'

resp = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term=' + search)
file = resp.json()
# print(json.dumps(resp.json(), indent=2))
for result in file['results']:
    print(result['trackName'])

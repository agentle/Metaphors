import requests
import json

# TODO: replace with your own app_id and app_key
app_id = '1ed9cb40'
app_key = '8da93db3cf0b498826a3768e850377e9'

language = 'en'
word_id = 'software'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))

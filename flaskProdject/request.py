import requests
import json
url = 'http://127.0.0.1:5000/store'
myobj = {'name': 'somevalue'}

x = requests.post(url, data = json.dumps(myobj))

print(x.text)
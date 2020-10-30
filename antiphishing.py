#Anti phishing spammer by Azure

import requests
import os
import random
import string
import json

print("[*] Phishing page spammer by Azure | Darktropical")
print("[*] Type \'example\' below for example exploit")

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = input("[*] Phishing link: \n[*] ")
if url == str("example"):
	url = "http://example.com"
elif url == str("Example"):
	url = "http://example.com"

names = json.loads(open('nameslist.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={

		'empty': username,
		'empty': password

		})

	print ("[*] Sending username",username, "and password",password)

#Follow video tutorial on how to setup ^^
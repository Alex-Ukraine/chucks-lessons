import urllib.request, urllib.parse, urllib.error
import json
import os.path
from os import path

# Not that is increasibgly requiring keys
# for this API

url = 'https://data.gov.ua/dataset/59ecf2ab-47a1-4fae-a63c-fe5007d68130/resource/21efcac7-6dd3-4d6e-8ff7-f8cd962cf3f9/download/mvswantedperson_photo_555.json'

id = "303095725"

print('Retrieving', url)
filename = 'mvswantedperson_photo_555.json'
if path.exists(filename):
	js = open(filename, 'r', encoding='utf-8')
	js = json.loads(js)
else:
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	js = json.loads(data)
	with open(filename, 'w', encoding='utf-8') as outfile:
		json.dump(data, outfile, indent=4)

#print('Retirieved', len(js), 'characters')

print(js[:100])
#for j in js:
	#print(j[:100])
	#if j["ID"] == id:
	#	opp = j["OPPHOTO1"]
	#	photo = j["PHOTO1BASE64ENCODE"]
	#	print('OPPHOTO1', opp, 'PHOTO1BASE64ENCODE', photo)
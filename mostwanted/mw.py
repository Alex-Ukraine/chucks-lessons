import json
with open('mostwanted.json', encoding='utf-8-sig') as input:
	info = json.loads(input.read())
print('count:', len(info))
for item in info:
	print(item['SEX'])

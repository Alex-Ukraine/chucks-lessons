fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname, encoding='utf8')

di = dict()
for lin in hand:
	lin = lin.rstrip()
	# print(lin)
	wds = lin.split()
	print(wds)
	for w in wds:
		# idiom: retrieve/create/update counter
		di[w] = di.get(w,0) + 1

# print(di)

tmp = list()
for k,v in di.items():
	newt = (v,k)
	tmp.append(newt)

# print('Flipped', tmp)
tmp = sorted(tmp, reverse=True)
# print('Sorted', tmp[:5])

for v,k in tmp[:5]:
	print(k,v)
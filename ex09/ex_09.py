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

# now we want to find the most common word
largest = -1
theword = None
for k,v in di.items():
	print(k,v)
	if v > largest:
		largest = v
		theword = k

print('Done', theword, largest)

c = {'a': 10, 'b':1, 'c': 22, 'd': 0}

print(sorted([ (v,k) for k,v in c.items()][:3], reverse=True))
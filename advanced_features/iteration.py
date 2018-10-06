def findMinAndMax(L):
	if L != 0:
		max = L[0]
		min = L[0]

		for i in L:
			if max < i:
				max = i
			if min > i:
				min = i
		return(min,max)
	else:
		return(None,None)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)

for value in d.values():
	print(value)

for k, v in d.items():
	print(k)
	print(v)

for i, value in enumerate(['A','B','C']):
	print(i,value)
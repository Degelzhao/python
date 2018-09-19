def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def calc(numbers):
	sum = 0 
	for n in numbers:
		sum = sum + n * n
	return sum


def add_end(L = None):
	if L is None:
		L = []
	L.append('END')
	return L


def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args,**kw))

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args,**kw))

	
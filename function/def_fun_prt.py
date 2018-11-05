import math

def quadratic(a,b,c):
	p = b*b - 4*a*c
	if p >= 0 and a != 0:
		x1 = (-b + math.sqrt(p)) / (2*a)
		x2 = (-b - math.sqrt(p)) / (2*a)
		print('this equation has two real roots: ')
		return x1,x2
	elif a == 0:
		x1 = x2 = -c/b
		print('this equation has one real roots: ')
		return x1
	else:
		return('Wrong Number!')

if __name__ == '__main__':
	a = float(input('please input a = '))
	b = float(input('please input b = '))
	c = float(input('please input c = '))
	print(quadratic(a,b,c))

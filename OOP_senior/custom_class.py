#定制类

'Custom class'


#__str__(),__repr__()

__author__ = 'Degel zhao'

class Student1(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name : %s)' %self.name
	__repr__ = __str__

#__str__:当重构__str__方法后，当使用print输出对象时，只要自己定义了__str__(self)方法，就会打印从这个方法中return的数据
#__repr__:当重构__repr__方法后，不管直接输出对象还是通过print打印的信息都按我们__repr__方法中定义的格式进行显示


#__iter__()
class Fib1(object):
	def __init__(self):
		self.a, self.b = 0, 1  # 初始化两个计数器a，b

	def __iter__(self):
		return self            # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a ,self.b = self.b, self.a + self.b   # 计算下一个值
		if self.a > 10000:                         # 退出循环的条件
			raise StopIteration()
		return self.a                              # 返回下一个值

#test:
#>>>for n in Fib():
#.......print(n)
#...
#1
#1
#2
#3
#5
#8
#13
#21
#34
#55
#89
#...
#6765

#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
#然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

#__getitem__()
class Fib2(object):
	def __getitem__(self,n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a


class Fib3(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a

		if isinstance(n,slice):        #n是切片
			start = n.start            #切片开始
			stop = n.stop              #切片结束
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:         #如果切片的位置在开始的后面
					L.append(a)
				a, b = b, a + b
			return L
#如果在类中定义了__getitem__()方法，那么它的实例对象(假设为P)就可以这样P[key]取值。
#当实例对象做P[key]运算时，就会调用类中的__getitem__()方法
#并且可以做切片操作


#__getattr__()
class Student2(object):
	def __init__(self):
		self.name = 'Michael'

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
#_getattr__是python里的一个内建函数，可以很方便地动态返回一个属性；
#当调用不存在的属性时，Python会试图调用__getattr__(self,'key')来获取属性，并且返回key


#__class__()
class Student3(object):
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print('My name is %s' %self.name)

#__class__()
#当一个类型实现了特殊方法__call__,该类的实例就变成了可调用的类型
#对象名()等价于 对象名.__call__()
#有时候可以简化对象的调用，让对象变成可调用的对象，实现__call__即可
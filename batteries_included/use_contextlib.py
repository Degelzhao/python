#并不是只有open()函数返回的fp对象才能使用with语句。
#实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句

from contextlib import contextmanager

class Query(object):

	def __init__(self,name):
		self.name = name

	def query(self):
		print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')

with create_query('Bob') as q:
	q.query()

@contextmanager
def tag(name):
	print("<%s>"%name)
	yield
	print("</%s>"%name)

with tag("h1"):
	print("hello")
	print("world")

#代码执行顺序是:
#1.with 语句首先执行yield之前的语句，打印出<h1>
#2.yield调用会执行with语句内部的所有语句，打印出hello和world
#3.最后执行yield之后的语句，打印出</h1>

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
	for line in page:
		print(line)
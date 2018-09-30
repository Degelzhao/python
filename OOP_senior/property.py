#使用@property

'use @property'

__author__ = 'Degel zhao'


class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value


class Screen(object):

	@property               
	def width(self):           #设置一个属性，把方法变为属性
		return self._width     #这里self._width只是为了区分上面的属性width才加的下划线，表示返回属性width的值

	@width.setter	
	def width(self,width):
		if not isinstance(width,(int,float)):
			raise ValueError('width must be a number!')
		self._width = width

	@property
	def height(self):
		return self._heigth

	@height.setter
	def height(self,height):
		if not isinstance(height,(int,float)):
			raise ValueError('height must be a number')
		self._heigth = height

	@property
	def resolution(self):      #对于resulution属性只设置了可读属性，因为后面并没有setter
		return self._width * self._heigth

#小结:
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性


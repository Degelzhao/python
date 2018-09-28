#访问限制

class Student(object):
	def __init__(self,name,gender):
		self.name = name
		self.__gender = gender

	def get_gender(self):
		return self.__gender

	def set_gender(self,gender):
		if gender in ['female','male']:
			self.__gender = gender
		else:
			raise ValueError('bad gender!')

#在属性名称前，加上两个下划线__,可以让内部属性不被外部访问
#如果要获取属性内容，可以加get_属性名，用这样的方法获取
#可以增加set_属性名的方法修改属性的值，这样做可以同时对参数做检查，避免传入无效的参数	    
	    	


#获取对象信息

'get object information'

__author__ = 'Degel zhao'

class Object(object):
	def __init__(self):
		self.x = 9                        #这个类有一个属性x,并把该属性的值设为9

	def calc(self):
		return self.x * self.x

def main():
	xuan = Object()                       #Object()对象的一个实例

	result1 = hasattr(xuan,'x')           #hasattr()用于判断xuan这个对象是否有属性x
	result2 = getattr(xuan,'x')           #getattr()用于获取xuan这个对象的x属性的值
	print((result1,result2))

	result3 = hasattr(xuan,'y')           #用于判断xuan这个对象是否有属性y,很明显没有 类My_Object的__init__只定义了x属性
	result4 = getattr(xuan,'y',404)       #当对象xuan没有属性y时就会输出默认值404
	setattr(xuan,'y',11)                  #给对象xuan设置新的属性y并赋值11,这时xuan这个对象有了x,y两个属性
	restlt3i = hasattr(xuan,'y')
	result4i = getattr(xuan,'y')
	print((result3,result4))
	print((restlt3i,result4i))
	#getattr(xuan,'y')                     #当一个对象没有属性y时，就会报属性错误 AttributeError

	setattr(xuan,'z',10)                  #给对象xuan设置新的属性z并赋值10,这时xuan这个对象有了x,y,z三个属性
	result5 = hasattr(xuan,'z')
	result6 = getattr(xuan,'z')
	print((result5,result6))

main()

  


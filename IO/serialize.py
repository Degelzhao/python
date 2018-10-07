#json的使用方法

'use_json'

__author__ = 'Degel zhao'

import json

class Student1(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score


def student1dict(std):
	return{
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

s = Student1('Bob',20,88)
print(json.dumps(s,default = student1dict))



class Student2(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

def student2dict(std):
	return{
		'name':std.name,
		'age':std.age
	}

s = Student2('小明',20)
print(json.dumps(s,ensure_ascii = True,default = student2dict))  #ensure_ascii = True表示输出中所有传入的非ascii字符都转义
print(json.dumps(s,ensure_ascii = False,default = student2dict)) #ensure_ascii = False表示这些字符将按原样输出

 

class Student3(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

s = Student3('emberspirit','25')
print(json.dumps(s,default = lambda obj: obj.__dict__))  #使用匿名函数将实例变为dict
s = Student3('火猫','25')
print(json.dumps(s,ensure_ascii = False,default = lambda obj: obj.__dict__))


#序列化:把变量从内存中变成可存储或传输的过程称为序列化，在Python中叫pickling
#Python语言特定的序列化模块是pickle,但如果要把序列化搞得更通用、更符合web的标准，就可以使用json模块
#json模块的dumps()和loads()函数是定义得非常好的接口的典范:
#	当我们使用时，只需要传入一个必须的参数
#	当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则
#	既做到了接口简单易用，又做到了充分的扩展性和灵活性
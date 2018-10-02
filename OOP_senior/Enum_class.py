#枚举类

'Enum class'

from enum import Enum, unique

__author__ = 'Degel zhao'

@unique
class Gender(Enum):
	Male = 0
	Female = 1

class Student(object):
	def __init__(self,name,gender):
		self.name = name
		self.gender = gender

# 测试:
lilei = Student('lilei', Gender.Male)
hanmeimei = Student("hanmeimei", Gender.Female)
if lilei.gender == Gender.Male and hanmeimei.gender == Gender.Female:
    print('测试通过!')
else:
    print('测试失败!')



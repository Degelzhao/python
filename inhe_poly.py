#继承和多态

'inheritance and polymorphism'

__auothor__ = 'Degel zhao'


class Animal(object):
	def run(self):
		print('Animal is running...')


class Dog(Animal):
	def run(self):
		print('Dog is running...')

	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')


#多态性:
def run_twice(animal):
	animal.run()
	animal.run()

#test1:
#>>>from inhe_poly import Animal
#生成一个实例:>>>animal = Animal()  
#传入Animal实例:>>>run_twice(Animal())
#打印结果:
#Animal is running...
#Animal is running...

#test2:
#>>>run_twice(Dog())
#Dog is running...
#Dog is running...

#test3:
#>>>run_twice(Cat())
#Cat is running...
#Cat is running...

#test4:
#>>>run_twice(Tortoise())
#Tortoise is running slowly...
#Tortoise is running slowly...

#多态性总结:
#新增一个Animal的子类，不必对run_twice()做任何修改
#任何依赖Animal作为参数的函数或者方法都可以不加修改的正常运行
#开闭原则：
#调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的
#对扩展开放:允许新增Animal子类；
#对修改封闭:不需要修改依赖Animal类型的run_twice()等函数

#鸭子类型:
class stone:
	def run(self):
		print('this stone is seem like animal...')

#test:
#>>>from inhe_poly import stone
#>>>st = stone()
#>>>run_twice(stone())
#this stone is seem like animal...
#this stone is seem like animal...

#鸭子类型总结:
#鸭子类型:一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定
#在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的
#在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的走和叫方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。

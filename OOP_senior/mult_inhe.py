#多重继承

'Multiple inheritance'

__author__ = 'Degel zhao'

class A(object):
	def foo(self):
		print('A foo')
	def bar(self):
		print('A bar')

class B(object):
	def foo(self):
		print('B foo')
	def bar(self):
		print('B bar')

class C1(A,B):
	pass

class C2(A,B):
	def bar(self):
		print('C2 - bar')

class D(C1,C2):
	pass

if __name__ == '__main__':
	print(D.__mro__)
	d = D()
	d.foo()
	d.bar()
	
#关于拓扑顺序
#1.从DAG途中选择一个没有前驱(即入度为0)的顶点并输出
#2.从图中删除该顶点和所有以它为起点的有向边
#3.重复1和2直到当前DAG图为空或当前途中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环

#根据拓扑顺序，可以分析出此多重继承的继承顺序:
#{D,C1,C2,A,B,object}
#d.foo():D => C1 => A
#d.bar():D => C1 => C2
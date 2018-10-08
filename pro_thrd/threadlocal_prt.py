'threading local practice'

__author__ = 'Degel zhao'


import threading

local = threading.local()

class Stud():
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

def get_info():
	std = local.student
	print('this is %s,age = %d, score = %d need by %s deal'%(std.name,std.age,std.score,threading.current_thread().name))

def set_info(name,age,score):
	local.student = Stud(name,age,score)
	get_info()


if __name__ == '__main__':
	t1 = threading.Thread(target=set_info, args=('Alice', 25, 88), name='Thread_1')
	t2 = threading.Thread(target=set_info, args=('Bob', 27, 90), name='Thread_2')
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print('print complete....')


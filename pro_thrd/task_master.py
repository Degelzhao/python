#分布式进程

import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
	pass

def return_task_queue():
	global task_queue
	return task_queue

def return_result_queue():
	global result_queue
	return result_queue

def test():
	#把两个Queue都注册到网络上, callable参数关联了Queue对象:
	#windows10 64不支持callable下调用匿名函数lambda,需要封装一下
	#QueueManager.register('get_task_queue', callable=lambda: task_queue)
	#QueueManager.register('get_result_queue', callable=lambda: result_queue)
	QueueManager.register('get_task_queue', callable=return_task_queue)
	QueueManager.register('get_result_queue', callable=return_result_queue)

	# 绑定端口5000, 设置验证码'abc':端口冲突照成Error: [WinError 10013] ，端口换为：6000
	manager = QueueManager(address=('127.0.0.1', 6000), authkey=b'abc') #ip地址为空会造成OSError: [WinError 10049]
	
	# 启动Queue:
	manager.start()
	# 获得通过网络访问的Queue对象:
	task = manager.get_task_queue()
	result = manager.get_result_queue()
	# 放几个任务进去:
	for i in range(10):
		n = random.randint(0, 10000)
		print('Put task %d...' % n)
		#将任务put到queue里
		task.put(n)  

	# 从result队列读取结果:
	print('Try get results...')
	for i in range(10):
		#从queue get到结果
		r = result.get(timeout=20)
		print('Result: %s' % r)
	# 关闭:
	manager.shutdown()
	print('master exit.')

if __name__ == '__main__':
	test()


#127.0.0.1是回送地址，指本地机，一般用来测试使用，主要用于网络软件测试以及本地机进程间通信，无论什么程序，一旦使用回送地址发送数据，协议软件立即返回，不进行任何网络传输
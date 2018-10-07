#fork():

#fork()调用一次，返回两次
#子进程永远返回0，而父进程返回子进程的ID
#一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID



#multiprocessing:
from multiprocessing import Process   #multiprocessing模块提供了一个Process类来代表一个进程对象
import os

def run_proc(name):
	print('Run child process %s (%s)...'%(name,os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.'%os.getpid()) #getpid():拿到当前进程的id
	p = Process(target=run_proc, args=('test',))
	print('Child process will start.')
	p.start()                               #创建一个子进程
	p.join()                                #等待子进程结束后再继续往下运行，用于进程间的同步
	print('Child process end.')

#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单
#getpid():拿到当前进程的id
#getppid():拿到父进程的id


#Pool:
from multiprocessing import Pool
import time, random

def long_time_task(name):
	print('Run task %s (%s)...'%(name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.'%(name, (end - start)))

if __name__ == '__main__':
	print('Parent process %s.'%os.getpid())
	p = Pool(8)                                    #创建一个进程池pool,并设定进程的数量为8
	for i in range(8):
		p.apply_async(long_time_task, args=(i,))   #将这8个对象提交到pool中，当一个进程执行完毕后会添加新的进程进去
	print('Waiting for all subprocesses done...')
	p.close()                                      #关闭pool,使其不再接受新的任务
	p.join()                                       #主进程阻塞，等待子进程的退出
	print('All subprocesses done.')

#Pool的默认大小是CPU的核数
#apply_async:异步非阻塞，意思就是:不用等待当前进程执行完毕，随时根据系统调度来进行进程切换


#进程间的通信
from multiprocessing import Queue

#写数据进程执行的代码
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

#读数据进程执行的代码
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)


if __name__=='__main__':
	#父进程创建Queue,并传给各个子进程
	q = Queue()
	#创建一个Process的实例
	pw = Process(target=write, args=(q,))  
	pr = Process(target=read, args=(q,))
	#启动子进程pw，写入:
	pw.start()
	#启动子进程pr，读取:                             
	pr.start()
	#主进程阻塞，等待子进程的退出
	pw.join()
	#pr进程里是死循环，因为没有给出具体的timeout，所以无法等待其结束，只能强行终止
	pr.terminate()

#Queue的使用:
#Queue是多进程安全的队列,可以使用Queue实现多进程之间的数据传递,提供了Put和Get两个方法 
	#put方法将数据插入到队列中,有两个可循参数:blocked和timeout.如果blocked为True且timeout为正值,该方法会阻塞timeout长的时
		#间,直到队列有剩余空间.
	#如果超时,会抛出Queue.Full异常,如果block为Fasle且该队列已满,会直接抛出Queue.Full异常
		

	#Get方法从队列中读取并且删除一个数据,它同样有blocked和timeout两个参数,blocked为true,等待timeout长的时间,直到取到数据
		#如果未取到,抛出Queue.Empty异常,如果blocked为False,直接抛出Queue.Empty异常









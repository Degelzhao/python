#多线程


import time, threading

# 新线程执行的代码:
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)         #启动主线程
t = threading.Thread(target=loop,name='LoopThread')                        #传入执行函数和子线程的名字，创建一个thread的实例
t.start()                                                                  #启动子线程
t.join()                                                                   #主线程阻塞，等待子线程退出
print('thread %s ended.' % threading.current_thread().name)


#threading模块中的current_thread()函数，永远返回当前线程的实例，主线程实例的名字叫Mainthread,子线程的名字在创建时指定

#Lock

balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		#先获取锁
		lock.acquire()
		try:
			change_it(n)
		finally:
			#改完之后释放锁
			lock.release()

#传入执行函数和函数的参数，创建一个thread的实例
t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
#创建一个线程
t1.start()
t2.start()
#主线程阻塞，等待子线程退出
t1.join()
t2.join()
print('balance = ',balance)

#当多个线程同时操作同一个变量时，很有可能将变量改乱了，所以，需要给修改的地方上一把“锁”
#创建锁通过threading.Lock()实现
#当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后执行代码，其他线程就继续等待直到获得锁为止
#获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程
#用try...finally来确保锁一定会被释放


#锁的好处
#1>确保了某段关键代码只能由一个线程从头到尾完整地执行

#锁的坏处
#1>阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
#2>由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止


#小结
#多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。




















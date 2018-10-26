import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()               # 获取EventLoop的引用
tasks = [hello(), hello()]                    # 把两个coroutine封装起来
loop.run_until_complete(asyncio.wait(tasks))  # 把封装好的coroutine放到EventLoop中执行
loop.close()

#1.@asyncio.coroutine把一个generator标记为coroutine类型
#2.然后把这个coroutine扔到EventLoop中执行




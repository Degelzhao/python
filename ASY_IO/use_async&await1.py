# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后
# 在coroutine内部用yield from调用另一个coroutine实现异步操作
# 为了简化和更好的标识异步IO,从Python 3.5开始引入了新的语法async和await,可以让coroutine的代码更简洁易读
# 替换步骤:
#1.把@asyncio.coroutine替换为async
#2.把yield from替换为await

import time
import asyncio

now = lambda : time.time()

# async关键字定义了一个协程(coroutine)
async def do_some_work(x):
    print('Waiting: ', x)

start = now()
# 协程也是一种对象
coroutine = do_some_work(2)
# 协程不能直接运行，需要把协程加入到事件循环（loop），后者在适当的时候调用协程
loop = asyncio.get_event_loop()
# 将协程注册到时间循环，并启动时间循环
loop.run_until_complete(coroutine)

print('Time: ',now() - start)
loop.close()
#在Python中通过生成器generator来实现协程

def customer():            #customer是一个生成器，把customer传入函数produce()执行
    r = ''
    while True:
        n = yield r        #yield r其实是一个表达式，它的值为None
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 ok'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)      #启动生成器customer,执行send()函数时，是先给yield r赋值，然后执行yield后面的语句
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()              #关闭生成器customer

c = customer()
produce(c)

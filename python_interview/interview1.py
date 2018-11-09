# 1、一行代码实现1--100之和
sum = sum(range(0,101))
print(sum)

# 2、如何在一个函数内部修改全局变量
# 利用global 修改全局变量
a = 5

def fn():
    global a
    a = 4
fn()
print(a)

# 3、列出5个python标准库
# datetime:Python处理日期和时间的标准库。
# collections:Python内建的一个集合模块，提供了许多有用的集合类。
# Base64:是一种用64个字符来表示任意二进制数据的方法。
# hashlib:提供了常见的摘要算法，如MD5，SHA1等等。
# hmac:哈希算法
# os:提供了不少与操作系统相关联的函数
# sys:通常用于命令行参数
# re:正则匹配
# math:数学运算

# 4、字典如何删除键和合并两个字典
dic1 = {'name':'barry', 'age':25}
del dic1['name']

dic2 = {'name':'Degel'}
dic1.update(dic2)
print(dic1)

# 5、谈下python的GIL
# GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
# 使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。
# 如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。
# 所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。

# 多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，
# 所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大

# 6、python实现列表去重的方法
list1 = [1,1,2,3,4,2,1,5,6,5,7,9]
list2 = sorted(set(list1))

print(list2)
print(list1)

# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
# *arg 和 **kwargs主要用于函数定义。你可以将不定数量的参数传递给一个函数。这里不定的意思是:预先不知道，函数使用者会传递
# 多少个参数给你，所以在这个场景下使用这两个关键字。
# *arg:是用来发送一个参数列表给一个函数
# **kwargs:允许你将不定长度的键值对，作为参数传递给一个函数

# 8、python2和python3的range（100）的区别
# python2返回列表，python3返回迭代器，节约内存

# 9、一句话解释什么样的语言能够用装饰器?
# 函数可以作为参数传递的语言，可以使用装饰器

# 10、python内建数据类型有哪些
# 整型--int
# 字符串--str
# 列表--list
# 元组--tuple
# 字典--dict

# 11、简述面向对象中__new__和__init__区别
class A(object):
    def __init__(self):
        print('这是init的方法:', self)

    def __new__(cls):
        print('这是cls的ID:',id(cls))
        print('这是new的方法:',object.__new__(cls))
        return object.__new__(cls)
A()
print('这是类A的ID:',id(A))

# __init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数
# 1、__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
# 2、__new__必须要有返回值，返回实例化出来的实例，
# 这点在自己实现__new__时要特别注意，可以return父类（通过super(当前类名, cls)）__new__出来的实例，
# 或者直接是object的__new__出来的实例
# 3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，
# __init__不需要返回值
# 4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的
# __new__函数的第一个参数是cls来保证是当前类实例，如果是其他类的类名，；那么实际创建返回的
# 就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

# 12、简述with方法打开处理文件帮我我们做了什么？

f = open('hello.txt', 'rb')
try:
    print(f.read())
except:
    pass
finally:
    f.close()

# 打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open

# 写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，
# 都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close

with open('hello.txt', 'rb') as f:
    print(f.read())

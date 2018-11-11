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

# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
list1 = [1,2,3,4,5]
def fn(x):
    return x * x

list2 = map(fn,list1)

list3 = [value for value in list2 if value > 10]
print(list3)

# 14、python中生成随机整数、随机小数、0--1之间小数方法
# 随机整数：random.randint(a,b),生成区间内的整数
# 随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数
# 0-1随机小数：random.random(),括号中不传参

import random
import numpy as np
result1 = random.randint(0,10)
result2 = np.random.randn(5)
result3 = random.random()
print('正整数:',result1)
print('5个随机小数:',result2)
print('0-1随机小数',result3)

# 15、避免转义给字符串加哪个字母表示原始字符串？
# r , 表示需要原始字符串，不转义特殊字符

# 16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
import re
str = '<div class="nam">中国</div>'

res = re.findall(r'<div class=".*">(.*?)</div>', str)
print(res)

# findall(): 找到所有匹配的字符串并返回

# 17、python中断言方法举例
# assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错

a = 3
assert(a > 1)
print('断言成功，程序继续进行!')

b = 4
assert(b > 3)
print('断言失败，程序报错!')

# 18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
# select distinct name from student
# 在表中，可能会包含重复值。
# 这并不成问题，不过，有时您也许希望仅仅列出不同（distinct）的值。关键词 distinct用于返回唯一不同的值。

# 19、10个Linux常用命令
# ls  pwd  cd  touch  rm  mkdir  tree  cp  mv  cat  more  grep  echo

# 20、python2和python3区别？列举5个
# 1>Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')
#   Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'
# 2>python2 range(1,10)返回列表，python3中返回迭代器，节约内存
# 3>python2中使用ascii编码，python中使用utf-8编码
# 4>python2中unicode表示字符串序列，str表示字节序列
#   python3中str表示字符串序列，byte表示字节序列
# 5>python2中为正常显示中文，引入coding声明，python3中不需要
# 6>python2中是raw_input()函数，python3中是input()函数

# 21、列出python中可变数据类型和不可变数据类型，并简述原理
# 不可变数据类型：数值型、字符串型string和元组tuple
# 不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，
# 在内存中则只有一个对象（一个地址），如下图用id()方法可以打印对象的id

c = 3
d = 3
print(id(c))
print(id(d))

# 可变数据类型：列表list和字典dict;
# 允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不
# 会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，在内存中则会
# 存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存
# 在引用计数，是实实在在的对象。

c = [1,2]
d = [1,2]
print(id(c))
print(id(d))

# 22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort()
res = ''.join(s)
print(res)

# set():创建一个无序不重复元素集

# 23、用lambda函数实现两个数相乘
sum = lambda a,b:a*b
print(sum(3,4))

# 24、字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
dict1 = {"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
list = sorted(dict1.items(),key = lambda i:i[0])
print('根据字典键排序:', list)

new_dict = {}
for i in list:
    new_dict[i[0]] = i[1]    # 字典赋值，左边为key，右边为value
print('新字典:', new_dict)

# 25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter
a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)

# 26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"
import re
a = "not 404 found 张三 99 深圳"
list = a.split(" ")
print(list)
res = re.findall('\d+|[a-zA-Z]+', a)
for i in res:
    if i in list:
        list.remove(i)

new_str = " ".join(list)
print(res)
print(list)

# 27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(x):
    return x % 2 == 1

new_list = filter(fn, a)
new_list = [i for i in new_list]
print(new_list)

# 28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [i for i in a if i % 2 == 1]
print(new_list)

# 29、正则re.complie作用
# re.compile是将正则表达式编译成一个对象，加快速度，并重复使用

# 30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
print(type((1,)))      # tuple
print(type((1)))       # int
print(type(("1")))     # str


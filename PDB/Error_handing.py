#错误调式

'Error handing'

__author__ = 'Degel zhao'

#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：

from functools import reduce

def str2num(s):
	try:
		int(s)
	except ValueError as e:
		print('ValueError:',e)
		return float(s)
	else:
		return int(s)
	

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main1():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main1()


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main2():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main2()
print('END')

#小结:
#1>需要掌握try...except...的用法
#2>可以返回多个except来捕捉多种错误类型(比如ValueError,ZeroDivisionError等等)
#3>如果遇到函数之间调用的只需要在恰当的函数里捕捉错误就可以了
#4>当多个函数有调用关系时某一个函数可能出错，不需要在上级调用它的函数都一一捕捉，只需要在合适的层次捕捉错误就可以了
#5>如果我们想让出错的同时抛出错误信息，同时程序可以继续运行，我们可以使用logging
#6>Python的错误其实也是class，所有的错误类型都继承自BaseException
#所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”


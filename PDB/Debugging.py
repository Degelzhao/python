#调试

'Debugging'

__author__ = 'Degel zhao'

#assert:

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main1():
    foo('0')

main1()

#logging
import logging
logging.basicConfig(level = logging.error)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#作用：
#logging允许你输出debug，info，warning，error等几个级别

#pdb

#python -m pdb pgmname:启动python调试器
#输入l来查看代码
#输入命令n可以单步执行代码
#任何时候都可以输入命令p 变量名来查看变量
#输入命令q结束调试，退出程序


#pdb.set_trace()

#这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，
#在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点

#运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，
#可以用命令p查看变量，或者用命令c继续运行

#pdb 和pdb.set_trace()参考程序err.py





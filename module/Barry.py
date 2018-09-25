#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a testing module'

__author__ = 'Degel zhao'


def sum(a,b):
	return a + b

if __name__ == "__main__":
	print('Barry的计算结果是:',sum(1,1))
	

#if __name__ == "__main__"实现的功能就是Make a script importable and executable,
#也就是说可以让模块既可以导入到别人的模块中，并且不影响别人模块的输出，另外该模块自己也可以用

#在大型工程中，常常有if __name__ == "__main__":来表明整个工程开始运行的入口
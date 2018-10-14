import itertools

'calculate PI'

__author__ = 'Degel zhao'

def pi(N):
	#创建一个奇数序列:
	na = itertools.count(1,2)
	#取该序列的前N项:
	na = itertools.takewhile(lambda x: x <= 2*N-1,na)
	#添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
	sum = 0
	for i in na:
		sum = sum + (-1)**((i+1)/2-1) * 4/i # (-1)**((i+1)/2-1)表示-1的n-1次方
	#求和:
	return sum

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

#小结:
#itertools模块提供的全部是处理迭代功能的函数，他们的返回值不是list,而是Iterator,只有用for循环迭代的时候才真正计算

#itertools模块:

#count()函数:可创建一个无限迭代器
#输入参数是start,从哪开始;
#step:每隔几个输出一个，默认为0

#cycle()函数:创建一个无限迭代器
#作用:把传入的序列无限循环输出
#>>> import itertools
#>>> cs = itertools.cycle('AB')                    # 注意字符串也是序列的一种
#>>> for c in cs:
#...     print(c)
#...
#'A'
#'B'
#'A'
#'B'
#'A'
#'B'
#...

#repeat()函数:同样创建一个无限迭代器
#作用:把一个元素重复指定次数
#>>> ns = itertools.repeat('A', 5)
#>>> for n in ns:
#...     print(n)
#...
#A
#A
#A
#A
#A

#takewhile()函数:可以为无限序列添加条件，拿取有限序列
#>>> natuals = itertools.count(1)
#>>> ns = itertools.takewhile(lambda x: x <= 15, natuals)
#>>> list(ns)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 

#chain()函数:把一组迭代对象组合成更大的迭代器
#>>>import itertools
#>>>for c in itertools.chain('AB','12'):
#...    print(c)
#...
#A 
#B 
#1 
#2

#groupby()函数:将迭代器中的元素进行分组，如果相同的相邻元素会分成一组
#>>>import itertools
#>>>for key, group in itertools.groupby('AA2222BBAA'):
#...    print(key, list(group))
#...
#A ['A', 'A'] 
#2 ['2', '2', '2', '2'] 
#B ['B', 'B'] 
#A ['A', 'A']



#文档测试

'document test'

__author__ = 'Degel zhao'


def fact(n):
	'''
	Function to get n!
	Example:
	>>> fact(1)
	1
	>>> fact(2)
	2
	>>> fact(3)
	6
	>>> fact('a')
	Traceback(most recent call last)
		...
	KeyError: 'a'
	'''

	if n < 1:
		raise ValueError()

	if n == 1:
		return 1
	return n * fact(n-1)

if __name__ == 'main':
	import doctest
	doctest.testmod()

print(fact(5))


# 小结
# 1>Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
# 2>doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确
# 3>只有测试异常的时候，可以用...表示中间一大段烦人的输出
# 4>最后3行代码。当模块正常导入时，doctest不会被执行。
#   只有在命令行直接运行时，才执行doctest。所以，不必担心doctest会在非测试环境下执行
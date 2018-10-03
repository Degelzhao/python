#单元测试

'unit test'

__author__ = 'Degel zhao'


import unittest          #引入python自带的unittest模块

from my_abc import Dict

class TestDict(unittest.TestCase):

	def test_init(self):
		d = Dict(a = 1,b = 'test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key,'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']


	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

if __name__ == '__main__':
	unittest.main()


#以test开头的方法就是测试方法，相反，则不是
#对每一类测试都需要编写一个test_xxx()方法
#unittest.TestCase提供了很多内置的条件判断，比如最常用的断言assertEqual()


#单元测试

'procedure to be tested'

__author__ = 'Degel zhao'


class Dict(dict):

	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self,key,value):
		self[key] = value

#super():用于调用父类的一个方法
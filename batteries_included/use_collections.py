'collections'

__author__ = 'Degel zhao'

#nametuple
from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print('Point:',p.x,p.y)

#namedtuple是一个函数，用来创建一个自定义的tuple对象
#并且规定了tuple元素的个数
#可以用属性而不是索引来引用tuple的某个元素


#deque
from collections import deque

q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

#deque是为了高效实现插入和删除操作的双向列表，适合队列和栈

#defaultdict
from collections import defaultdict

dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =',dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

#defaultdict:如果希望key不存在时，返回一个默认值，就可以用default
#默认值时调用函数返回的，而函数在创建defaultdict对象时传入

#OrderedDict

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

#使用dict时，Key是无序的，如果要保持Key的顺序，可以用OrderedDict

of = OrderedDict()
of['z'] = 1
of['y'] = 2
of['x'] = 3
list(of.keys())
print(of)
#OrderedDict的key会按照插入的顺序排列，不是key本身顺序

#Counter

from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)

#Counter是一个简单的计数器，可以统计字符出现的个数
#Counter实际上也是dict的一个子类
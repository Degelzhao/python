'StringIO and BytesIO'

__author__ = 'Degel zhao'


#在内存中读写str

from io import StringIO

#StringIO()无参数
f = StringIO()        #创建一个StringIO
f.write('hello')
f.write(' ')
f.write('world')

print(f.getvalue())   #获得写入后的str

#StringIO有内容，然后像文件一样读取
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

#在内存中读写bytes
from io import BytesIO

#BytesIO无参数
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

#BytesIO有参数
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
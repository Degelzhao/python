'use struct'

__author__ = 'Degel zhao'

#struct模块可以解决bytes和其他二进制数据类型的转换
#struct的pack函数把任意数据类型变成bytes
#struct的unpack把bytes变成相应的数据类型
import base64,struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info1(data):
	h = struct.unpack('<ccIIIIIIHH',data[:30])   #使用unpack转换为需要的数据类型
	if h[0] == b'B' and (h[1] == b'M' or h[1] == b'A'):
		print(True)
		print('位图大小: ',h[6],'*',h[7], '颜色数: ',h[9])
	else:
		print(False)

def bmp_info2(data):
	f = open(str,'rb')
	s = f.read(30)
	h = struct.unpack('<ccIIIIIIHH',s)
	if h[0] == b'B' and h[1] in (b'M',b'A'):
		print(True)
		print('位图大小: ',h[6],'*',h[7], '颜色数: ',h[9])
	else:
		print(False)

if __name__ =='__main__':
	bmp_info1(bmp_data)
	str = input('please the way of your file')
	bmp_info2(str)

#b'B'(h[0])、(b'M' or b'A') is h[1] 说明是Windows位图

#操作方式:
#C:\work\python\batteries_included>python use_struct.py
#True
#位图大小:  28 * 10 颜色数:  16
#please the way of your file.\love.bmp
#True
#位图大小:  1094 * 516 颜色数:  24
'os module'

__author__ = 'Degel zhao'

#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径

import os

keyword = input('Input keyword: ')
up = '.'
result = []

def check(up, keyword):
	all = os.listdir(up)   #返回up指定的文件夹包含的文件或文件夹的名字的列表
	for x in all:
		try:
			abs_x = os.path.join(up, x)     #拼接路径
			if os.path.isdir(abs_x):        #判断abs_x是否是已经存在的目录
				up = os.path.join(up, x)    #存在的话，拼接路径
				check(up, keyword)
				up = os.path.split(up)[0]   #将地址分割成目录和文件名返回
			if os.path.isfile(abs_x):       #判断abs_x是否是文件  
				if keyword in x:            #判断关键字是否在路径当中
					result.append(abs_x)    #追加路径

		except:
			continue

check(up, keyword)
#打印出路径的总条数
print('\n==========Find %d files==========\n' % len(result))
#循环将找到的路径打印出来
num = 0
for r in result:
	num += 1
	print('%d  %s' % (num, r))
print('\n===============END===============\n')
os.system("pause")

















































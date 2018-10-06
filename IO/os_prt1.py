import os
import time
import re

dirpath = r'C:/work/python'
listFile(dirpath)
findFile(dirpath,'.py')

def listFile(path):
	print('权限\t文件数\t用户名\t群组名\t大小\t月份\t日期\t时间\t文件名')
	for x in os.listdir(path):
		dir = os.path.join(path,x)
		st = os.stat(dir)  #获取dir指定路径的信息
		print(oct(st.st_mode)[-3:],end='\t')
		print(numOfFiles(dir),end='\t')
		print(st.st_uid,end='\t')
		print(st.st_gid,end='\t')
		print(st.st_size,end='\t')
		lc_time=time.localtime(st.st_mtime)
		print(time.strftime('%b',lc_time),end='\t')
		print(lc_time.tm_mday,end='\t')
		print(time.strftime('%H:%M',lc_time),end='\t')
		print(x)


def numOfFiles(path,num=1):
	try:
		for x in os.listdir(path):
			dir=os.path.join(path,x)
			if os.path.isdir(dir):
				num+=1
				num=numOfFiles(dir,num)

	except BaseException as e:
		pass
	finally:
		return num

listFile()



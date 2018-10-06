#文件的读写

'read and write for file'

__author__ = 'Degel zhao'



#打开文件需要进行关闭,一种方法是使用try...finally... 另外一种方法是使用with...open...as
def main1():
	try:
		file = open("C:/work/python/IO/Degel.txt",'r')
		print(file.read())
	finally:
		file.close()

main1()

#使用with和try...finally效果是一样的 但是代码更简单 而且不用写close()函数
def main2():
	with open("C:/work/python/IO/Degel.txt",'r') as file:
		print(file.read())

main2()

#readlines():一次读取所有内容并按行返回list
def main3():
	with open("C:/work/python/IO/Degel.txt",'r') as file:
		for line in file.readlines():
			print(line.strip())          #strip()函数去掉尾部\n

main3()

#文件的写入
def main4():
	with open("C:/work/python/IO/Degel.txt",'w') as file:
		file.write("hello Degel zhao")


main4()

#使用write,原本的内容会被覆盖掉，所以我们需要使用追加的方式:a
def main5():
	with open("C:/work/python/IO/Degel.txt",'a') as file:
		file.write("hello world")

main5()

#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
def main6():
	with open("C:/Users/asd/Pictures/AE86/timg.jpg",'rb') as file:
		print(file.read())

main6()

#小结
#在Python中，文件读写是通过open()函数打开的文件对象完成的。
#使用with语句操作文件IO是个好习惯

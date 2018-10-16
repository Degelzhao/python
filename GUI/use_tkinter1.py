#图形界面
#Python内置了Tkinter,Tkinter封装了访问图形库Tk的接口，通过Tkinter就能完成简单的GUI编程

#Tkinter
#创建一个GUI程序的步骤如下:
#1.导入Tkinter模块
#2.创建一个继承Frame的类(Frame是用来放控件的容器，可以理解为一个矩形框架)
#3.创建控件
#4.指定控件的master
#5.启动消息循环

from tkinter import *                 #引入Tkinter包的所有内容

class A(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()                   #把控件放到主界面，实现布局
		self.createWidgets()          #调用创建控件的方法

	def createWidgets(self):
		self.helloLabel = Label(self,text = 'Hello, world!')  #创建label控件，用于显示文本或位图
		self.helloLabel.pack()        #把Label控件放到主界面
		self.quitButton = Button(self,text = 'Quit', command = self.quit)   #创建button控件，用于退出
		self.quitButton.pack()

app = A()                             #实例化A
app.master.title('The first GUI')     #设置窗口标题
app.master.geometry('200x100')        #设置窗口大小
app.mainloop()                        #启动消息循环
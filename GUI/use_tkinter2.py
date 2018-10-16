#可以加入文本框，让用户输入文本，然后显示信息
#需要引入一个messagebox模块

from tkinter import *
import tkinter.messagebox as messagebox

class A(Frame):
	def __init__(self,master = None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)                   #Entry让用户输入文本
		self.nameInput.pack()                          #把Entry控件放到主界面
		self.alertButton = Button(self,text = 'Hello',command = self.hello)  #加入button控件，按钮用hello方法
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'         #拿取用户输入的文本
		messagebox.showinfo('Message','Hello, %s'%name)#弹出消息对话框

app = A()
app.master.title('Hello World')
app.mainloop()
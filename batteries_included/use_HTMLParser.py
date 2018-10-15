#解析HTML页面
'use HTMLParser'

__author__ = 'Degel zhao'

#HTMLParser是解析HTML文本的工具
#与解析XML类似，我们需要定义好标签处理的方法
#HTMLParser常用方法:
#handle_starttag(tag,attrs):处理开始标签，比如<head>
#handle_endtag(tag):处理结束标签，比如</head>
#handle_startendtag(tag,attrs):处理自己结束的标签，如<img/>
#handle_data(data):处理数据，标签之间的文本
#handle_comment(data):处理注释，<!-- -->之间的文本

#tag指标签，attrs指属性列表，以元祖tuple的方式展示

from html.parser import HTMLParser                 #引入HTML解析模块
from urllib import request                         #引入URL请求模块
import re                                          #引入正则表达式模块
from collections import OrderedDict

class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)                  #继承父类的属性
		self.is_time = False                       #初始化时间布尔值，用于判断标签
		self.is_title = False
		self.is_location = False
		self.is_year = False
		self.info = []                             #初始化一个list,用于储存获取的信息

	def handle_starttag(self,tag,attrs):           #定义开始标签处理器
		if tag == 'time':                          #判断标签是否表示时间，若是，更改布尔值，下面类似
			self.is_time = True

		if tag == 'h3' and ('class','event-title') in attrs:
			self.is_title = True

		if tag == 'span' and ('class','say-no-more') in attrs:
			self.is_year = True

	def handle_data(self,data):                    #定义数据内容处理器
		if self.is_time == True:                   #如果标签为时间
			self.is_time = False                   #初始化时间布尔值
			self.info.append(dict(会议时间=data))   #把数据储存在info中，下面类似操作标题，地点，年份

		if self.is_title == True:
			self.is_title = False
			self.info.append(dict(会议名称=data))

		if self.is_location == True:
			self.is_location = False
			self.info.append(dict(会议地点=data))

		if self.is_year == True:
			self.is_year = False
			#由于网页源码中出现是年份标签但显示的内容不是年份，所以增加一个正则表达式来判断
			if re.match(r'[0-9]',data.strip()):    #[0-9]表示范围必须从大到小
				self.info.append(dict(会议年份=data))

def getinfo(data,u):                               #定义信息处理函数
	parser = MyHTMLParser()                        #创建HTML解析器
	parser.feed(data)                              #解析HTML文件
	count = 0
	print('抓取网址:%s\n抓取信息如下:'% u)
	for x in parser.info:                          #打印info
		for key in x:                              #由于info存的是dict组成的list,所以还要遍历dict
			print(key + ':' + str(x[key]))
		count += 1
		if count % 4 == 0:                         #当输出四个数据后，打印分割线
			print('-------------------------------')

web = 'https://www.python.org/events/python-events/'
with request.urlopen(web) as f:                    #打开网页
	Data = f.read()
	Data = Data.decode('utf-8')

getinfo(Data,web)                                  #解析文件并打印信息
'use XML to get weather from Yahoo'

__author__ = 'Degel zhao'

from xml.parsers.expat import ParserCreate       # 引入xml解析模块
from urllib import request                       # 引入URL请求模块

class WeatherSaxHandler(object):                 # 定义一个天气时间处理器
	weather = {'city':1, 'forecast':[]}          # 初始化城市city和预报信息forecast

	def start_element(self, name, attrs):        # 定义开始标签处理事件 
		if name == 'yweather:location':          # 获取location信息(yweather是python中的一个连接Yahoo的接口模块)
			self.weather['city'] = attrs['city'] 

		elif name =='yweather:forecast':         # 获取forecast信息
			self.weather['forecast'].append({
				'date':attrs['date'], 
				'high':attrs['high'], 
				'low':attrs['low']
			})

def parseXml(xml_str):                           # 定义xml解析器
	handler = WeatherSaxHandler()                # 创建一个事件处理器的实例
	parser = ParserCreate()                      # 创建一个解析器
	#给与开始标签的处理方式
	parser.StartElementHandler = handler.start_element     
	parser.Parse(xml_str)                        # 解析xml文本

	print('City: ' + handler.weather['city'])    # 打印city信息
	print('Weather: ')
	for x in handler.weather['forecast']:        # 打印天气信息
		print(x)

	return handler.weather

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
	data = f.read()

result = parseXml(data.decode('utf-8'))          # parseXml:解析为对应的xml文档
assert result['city'] == 'Beijing'

#XML:可扩展标记语言
#它是传输和存储数据常用的工具，在信息存储和描述领域十分流行

#操作XML的常用方法有：DOM和SAX
#DOM占用内存大，解析慢，但可以遍历任意节点
#SAX，占用内存小，解析快，但需要自己处理事件

#正常情况下，优先考虑SAX，因为DOM实在太占内存
#使用SAX：
#一般而言，定义好start_element，end_element和char_data三个事件即可

#在对应的事件中，定义好我们想要的处理方式
#然后通过ParserCreate()生成解析器
#使用parser.Parse解析文本即可

#XML生成
#用最简单的方法，append拼接

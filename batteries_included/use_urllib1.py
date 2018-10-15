'use urllib'

__author__ = 'Degel zhao'

#利用urllib读取JSON，然后将JSON解析为Python对象

from urllib import request
from contextlib import closing
import json

def fetch_data(url):
	#使用with-closing方法请求url,并读取url中的内容
	with closing(request.urlopen(url)) as f:
	#将读取的字节型文件，转化为字符串型
		text_json = f.readline()
	#使用json.loads函数将str-python对象
	return json.loads(text_json.decode('utf-8'))

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')

#urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应

#JSON函数:
#json.dumps:将Python对象编码成JSON字符串
#json.loads:将已编码的JSON字符串解码为Python对象

#小结
#urllib提供的功能就是利用程序去执行各种HTTP请求，在爬虫时经常用到这个库

#简单爬虫:
#1.引入urllib.request模块，这是一个请求模块
#2.通过urllib.request的urlopen()方法来打开一个网页
#3.使用read()方法来获取网页信息

#urllib.request.urlopen()函数参数介绍:
#urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
#常用的前3个参数:url,data,timeout
#url -- 需要打开的网址
#data -- 需要传入的数据，一般在get请求方式使用
#timeout -- 超时时间，当网络请求过慢，超过timeout设置的时间，就会给出异常，而不是一直等待结果
#模拟浏览器
#有时候，我们爬取网页的时候会出现错误，这是因为这些网页为防止恶意获取信息进行了反爬虫设置
#为避免这种情况，一般而言我们会模拟成浏览器去访问网页
#要模拟成浏览器，就需要添加Headers信息，即头信息。通过设置User-Agent可以让爬虫模拟成浏览器

#如何添加头信息呢?这里需要用到urllib模块中的urllib.request.Request()函数
#调用urllib.request.Request()可以创建一个request对象，调入时传入3个参数:
#1.url -- 网址信息
#2.数据，默认为0
#3.headers,即需要添加的头信息，要以dict类型传入，默认不传头部

import urllib.request

url = 'http://www.baidu.com'                            #设置url的值

header = {                                              #设置header的值
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
}

request = urllib.request.Ruquest(url,headers = header)  #调用Request()函数
data = urllib.request.urlopen(request).read()           #访问网页

with open('./1.html','wb') as fh:                       #创建html文件并把数据保存下来
	fh.write(data)


#那怎样得到User - Agent的信息呢?
#1.使用浏览器打开任意网页，按F12
#2.在弹出界面的上方找到 Network,点击后会出现一些文件，点击其中的一个，点击右边的header,在里面就有User - Agent信息
from wsgiref.simple_server import make_server   # 引入wsgiref模块中的make_server函数
from WSGI_hello import application              # 引入application函数

httpd = make_server('', 8888, application)      # 创建一个服务器
print('Serving HTTP on port 8888..')
httpd.serve_forever()                           # 开始监听HTTP请求

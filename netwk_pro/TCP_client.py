#TCP客户端

import socket

#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9999))
#接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Degel',b'Barry',b'Zhaowei']:
	#发送数据
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')           
#关闭socket
s.close()


           


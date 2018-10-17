#UDP:
#TCP是通过建立可靠连接，以流的方式传输数据
#而UDP则是面向无连接的协议，只需要知道目标的IP地址和端口号就能传输数据，无需建立连接
#优点:速度快
#缺点:不能保证数据能够到达

import socket
#SOCK_DGRAM指定socket类型是UDP，不用建立connect()连接,直接用sendto()发送
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in[b'Degel',b'Barry',b'zhaowe']:
	#发送数据
	s.sendto(data,('127.0.0.1',9999))
	#接收数据
	print(s.recv(1024).decode('utf-8'))
#关闭socket
s.close()
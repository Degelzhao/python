import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('Build UDP on 9999...')
while True:
	#返回数据和客户端的地址和端口
	data,addr = s.recvfrom(1024)
	print('Receive from %s:%s'%addr)
	#发送数据到客户端(addr是客户端地址和端口)
	s.sendto(b'Hello,%s!'%data,addr)
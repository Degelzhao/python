import socket,threading,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定需要监听的端口
s.bind(('127.0.0.1',9999))
#监听绑定的端口
s.listen(1)
print('Waiting for connecting...')
#接收客户端的连接
def tcplink(sock,addr):
	print('Accept new connecting from %s:%s...'% addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		#如果没有接收到数据或收到'exit',则退出
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello,%s!'%data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed'% addr)

while True:
	#接收客户端的连接和地址
	sock,addr = s.accept()
	#创建新线程来处理TCP连接
	t = threading.Thread(target = tcplink, args = (sock, addr))
	#启动线程
	t.start()

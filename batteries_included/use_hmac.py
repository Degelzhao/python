'use hamc'

__author__ = 'Degel zhao'

import hmac, random
#hmac加密
def get_hmac(key,pw):
	return hmac.new(key.encode('utf-8'),pw.encode('utf-8'),'MD5').hexdigest()

#账号密码处理
class User(object):
	def __init__(self,username,password):
		self.username = username
		self.key = ''.join([chr(random.randint(48,122)) for i in range(25)])
		self.password = get_hmac(self.key,password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

#验证登陆
def login(user,pwd):
	user = db[user]
	return user.password == get_hmac(user.key, pwd)

#测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

#hmac:将salt看作一个"口令",计算一段message的哈希时，根据不通口令计算出不同的哈希
#主要是将key混入计算过程中，要验证哈希，必须同时提供正确的口令

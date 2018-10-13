#use hashlib

#根据用户输入的口令是否正确，返回True或False

__author__ = 'Degel zhao'

import hashlib

#normal

def get_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

def calc_md5(password):
	return get_md5(password)

db = {
	'michael': 'e10adc3949ba59abbe56e057f20f883e',
	'bob': '878ef96e86145580c38c87f0410ad153',
	'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user,password):
	if db[user] == password:
		return True
	else:
		return False

if __name__ == '__main__':
	count = 0
	while count < 3:
		username = input('please input your username:')
		password = input('please input your password:')
		pwd = calc_md5(password)
		if login(username,pwd) == True:
			print('Welcome log!')
			count = 3
		else:
			print('Wrong username or password!')
			count += 1
			if count == 3:
				print('logon failure')
			else:
				print('you can try',3 - count,'times')

#摘要算法不是加密算法，不能用于加密(因为无法通过摘要反推明文),
#只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令

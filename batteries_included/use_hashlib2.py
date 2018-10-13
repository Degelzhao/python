#根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5(add Salt)
'use hashlib'

__author__ = 'Degel zhao'

import hashlib

def get_md5(str):
	md5 = hashlib.md5()
	md5.update(str.encode('utf-8'))
	return md5.hexdigest()

db = {}

def register(username,password):
	db[username] = get_md5(password + username + 'the-Salt')

def login(username,password):
	pwd = get_md5(password + username + 'the-Salt')
	if db[username] == pwd:
		return True
	else:
		return False

if __name__ == '__main__':
	username = input('please input your username:')
	password = input('please input your password:')
	register(username,password)
	print(login(username,password))
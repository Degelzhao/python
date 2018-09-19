#使用切片来完成trim操作

def trim(s):
	if s[:1] != ' ' and s[-1:] != ' ': #判断首尾是否为空	
		return s
	elif s[:1] == ' ':
		return trim(s[1:])
	elif s[-1:] == ' ':
		return trim(s[:-1])




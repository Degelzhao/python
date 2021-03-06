'use base64'

__author__ = 'Degel zhao'

#Base64是一种任意二进制到文本字符串的编码方式，常用于在URL,Cookie,网页中传输少量二进制数据
import base64
#能处理去掉=的base64解码函数
def safe_base64_decode(s):
	if len(s) % 4 == 0:
		return base64.urlsafe_b64decode(s) #解码为文本字符串
	s = s + b'='
	print('s = ',s)
	return safe_base64_decode(s)

print('s = %s'%(safe_base64_decode(b'YWZJAs')))

#参数s必须是3的倍数，因为二进制数据，每3个字节一组
#所谓Base64，就是说选出64个字符----小写字母a-z、大写字母A-Z、数字0-9、符号"+"、"/"（再加上作为垫字的"="，实际上是65个字符）----作为一个基本字符集。然后，其他所有符号都转换成这个字符集中的字符。
#转换方式可以分为4步:
#1>将每三个字节作为一组，一共是24个二进制位
#2>将这24个二进制位分为四组，每个组有6个二进制位
#3>在每组前面加两个00，扩展成32个二进制位，即四个字节

#Base64将三个字节转化成四个字节，因此Base64编码后的文本，会比原文本大出三分之一左右
#如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉
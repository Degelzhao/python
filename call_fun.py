import warnings
warnings.filterwarnings("ignore")

n1 = 255
n2 = 1000

print('n1 的十六进制表示为：',hex(n1))
print('n2 的十六进制表示为：',hex(n2))

d = ['255','1000']
for x in d:
	print(hex(int(x)))


d = ['255','1000']
n = 0
s = 1
while n < len(d):
	print('%d 的十六进制表示为：%s'%(int(d[n]),hex(int(d[n]))))
	n = n + 1
	s = s + 1

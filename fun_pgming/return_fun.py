#利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
	def f():
		n = 0
		while True:
			n = n + 1
			yield n
	sun = f()
	def counter():
		return next(sun)
	return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

#createCounter返回的是counter这个函数，而此时f()并没有执行并返回一个生成器对象。所以
#每次createCounter()都会得到一个counter函数，而执行counter(),都会执行f()而生成一个
#新的生成器对象
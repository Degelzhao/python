age = 17
if age >= 18:
	print('your age is',age)
	print('your age is %d'%age)
	print('adult')
else:
	print('your age is %d'%age)
	print('teenager')

#you should pay attention to add the colon(:) to
#the behind of IF and else

age = 3
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')

s = input('please your birthday:')
birth = int(s)
if birth < 2000:
	print('Before 00')
else:
	print('After 00')

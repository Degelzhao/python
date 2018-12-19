a = input('please input number a:')
b = input('please input number b:')

try:
    c = int(a) + int(b)
except ValueError:
    print('you must be input number!')
else:
    print(c)


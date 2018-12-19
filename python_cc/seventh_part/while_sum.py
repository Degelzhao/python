print("Give me two number, and i'll add them")
print("Enter 'q' to quit anywhere")

while True:
    a = input('please input first number:')
    if a == 'q':
        break
    b = input('please input second number:')
    if b == 'q':
        break
    try:
        c = int(a) + int(b)
    except ValueError:
        print('you must be input number!')
    else:
        print(c)
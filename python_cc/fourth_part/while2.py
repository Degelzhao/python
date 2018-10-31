'practice'

__author__ = 'Degelzhao'

# way 1

prompt = "please input your age or press 'quit' to exit: "
age = ''

while age != 'quit':
    age = input(prompt)

    if age != 'quit':
        if int(age) < 3:
            print('you can watch free movie')
        if int(age) >= 3 and int(age) <= 12:
            print('you need to pay 10 dollars')
        if int(age) > 12:
            print('you need to pay 15 dollars')

# way 2
prompt = "please input your age or press 'quit' to exit: "
active = True

while active:
    age = input(prompt)

    if age == 'quit':
        break
    elif int(age) < 3:
        print('you can watch free movie')
    elif int(age) >= 3 and int(age) <= 12:
        print('you need to pay 10 dollars')
    elif int(age) > 12:
        print('you need to pay 15 dollars')

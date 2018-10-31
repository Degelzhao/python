'practice'

__author__ = 'Degelzhao'

message = "\nplease input a number to testing"
message += "\nor you can input 'quit' to exit: "

active = True
while active:
    number = input(message)
    if number == 'quit':
        active = False
    if number != 'quit':
        if int(number) % 10 == 0:
            print('this number is divisible by 10')
        else:
            print('this number can not divisible by 10')
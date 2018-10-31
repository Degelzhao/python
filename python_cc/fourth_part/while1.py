'practice'

__author__ = 'Degelzhao'

# way 1

prompt = "\nplease input your pizza toppings"
prompt += "\nor input 'quit' to end your order: "

message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("we will add this " + message + " to pizza")
# way 2

prompt = "\nplease input your pizza toppings"
prompt += "\nor input 'quit' to end your order: "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print("we will add this " + message + " to pizza")

import json

def remember_number():
    filename = 'favorite_num.json'
    try:
        with open(filename, 'r') as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        number = input('please input your favorite number:')
        with open(filename, 'w') as f_obj:
            json.dump(number, f_obj)
        print("Your favorite number " + number + " has been stored!")
    else:
        print("I know your favorite number! It's " + number)

remember_number()
print('o')
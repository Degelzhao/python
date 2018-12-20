import json

filename = 'favorite_num.json'
number = input('please input your favorite number:')

with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

print("i know your favorite number! It's " + number)
print('oka')
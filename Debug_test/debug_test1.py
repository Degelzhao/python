validation_active = True

filename = 'guest_book.txt'
while validation_active:
    name = input('please input your name:')
    print('Thanks!')
    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')
    repeat = input('Would you like to let another person respond? (yes/no)"')
    print('Exit immediately')
    if repeat == 'no':
        validation_active = False
print('End')
filename = 'reason_pgm.txt'

while True:
    reason = input('Would you please tell me why you like programming?')
    with open(filename, 'a') as file_object:
        file_object.write(reason + '\n')
    repeat = input('Would you like to let another person response? (yes/no)')
    if repeat == 'no':
        break



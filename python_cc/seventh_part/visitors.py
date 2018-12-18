"write file practice"

__author__ = 'Aiolos Zhao'


name = input('please input your name:')
filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(name)

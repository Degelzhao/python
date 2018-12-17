"file practice"

__author__ = 'Aiolos Zhao'


filename = 'learning_python.txt'

# 第一次打印，读取整个文件
with open(filename) as file_object:
    contents = file_object.read()
    new = contents.replace('Python', 'C')
    print(new.rstrip())

print('\n')

# 第二次打印时遍历文件对象
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n')

# 第三次打印时将各行存储在一个列表中，再在with代码块外打印它们
with open(filename) as file_object:
    # 从文件中读取每一行，并将其存储在一个列表中
    lines = file_object.readlines()

file_len = len(lines)
print(file_len)

pi_string = ''
for line in lines:
    file_len = file_len -1
    if file_len == 0:
        pi_string += line.strip() + '.'
    else:
        pi_string += line.strip() + ','


print(pi_string)


def print_file(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        #print('Sorry, the file %s does not exist' %filename)
    else:
        print(contents)

filenames = ['dog.txt', 'cat.txt']
for filename in filenames:
    print_file(filename)
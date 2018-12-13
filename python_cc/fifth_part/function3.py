def show_magicians(magic_names):
    for magic_name in magic_names:
        print('Magician name:%s' % magic_name)


new_names = []
def make_great(magic_names):
    for magic_name in magic_names:
        current_name = 'the great' + ' ' + magic_name
        new_names.append(current_name)


magic_names = ['Aiolos', 'Degel', 'Lisa']
make_great(magic_names)
show_magicians(new_names)

# 可以使用function_name(magic_names[:])来向函数传递列表的副本而不是原件，这样函数所做的任何修改都只影响副本，而不
# 影响原件
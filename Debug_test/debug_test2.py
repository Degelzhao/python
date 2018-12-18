def your_name(first, last):
    link = first + ' ' + last
    return link

def your_hobby(hobby):
    fullname = your_name(first = 'Aiolos', last = 'Zhao')
    print('%s hobby is %s' % (fullname, hobby))

if __name__ == '__main__':
    your_hobby('music')

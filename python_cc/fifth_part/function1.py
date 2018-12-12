def make_shirt1(st_size, st_words):
    print('this T-shirt is %s size and printed %s.' %(st_size, st_words))

# 位置实参
make_shirt1('L','Hello')
# 关键字实参
make_shirt1(st_size='L',st_words='word')

def make_shirt2(st_size, st_words = 'I love Python'):
    print('this T-shirt is %s size and printed %s.'%(st_size, st_words))

make_shirt2('L')
make_shirt2('M')
make_shirt2('S')

def describe_city(city, country = 'China'):
    print('%s is in %s.' %(city, country))

describe_city('Baoji')
describe_city('Xian')
describe_city('NewYork', 'USA')

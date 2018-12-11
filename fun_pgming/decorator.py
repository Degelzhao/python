import functools

def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log1
def now1():
    print('2018-12-11')

now1()
print(now1.__name__)
print('\n')

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('hello')
def now2():
    print(2018-12-11)

now2()
print(now2.__name__)

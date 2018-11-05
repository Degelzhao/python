'practice class'

__author__ = 'Degelzhao'

class Dog():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_name(self):
        print('my dog name: %s' %(self.name.title()))

    def print_age(self):
        print('my dog age: %d' %(self.age))

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')

def main():
    dog = Dog('bibi',4)
    dog.print_name()
    dog.print_age()
    dog.sit()
    dog.roll_over()

if __name__ == '__main__':
    main()
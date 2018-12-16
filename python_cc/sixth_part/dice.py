from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides


    def roll_die(self):
        print('The current number of dice points is %s' %self.sides)
        print('Roll the dice:')
        x = randint(1,6)
        print('The number of points after shaking is %s' %x)


die = Die()
die.roll_die()
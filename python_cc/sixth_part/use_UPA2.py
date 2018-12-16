class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('this administrator first name is %s, last name is %s' %(self.first_name, self.last_name))

    def greet_user(self):
        print('hello %s %s!' %(self.first_name, self.last_name))
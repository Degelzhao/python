class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('restaurant name is ' + self.restaurant_name)
        print('the food is %s' %self.cuisine_type)

    def open_restaurant(self):
        print('the %s is open!' %self.restaurant_name)

restaurant = Restaurant('KFC', 'western type')
restaurant.describe_restaurant()
restaurant.open_restaurant()

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('this customer first name is %s, last name is %s' %(self.first_name, self.last_name))

    def greet_user(self):
        print('hello %s %s!' %(self.first_name, self.last_name))

user = User('Zhao', 'Wei')
user.describe_user()
user.greet_user()
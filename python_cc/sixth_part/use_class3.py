"practice"

__author__ = 'Aiolos Zhao'

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('restaurant name is ' + self.restaurant_name)
        print('the food is %s' %self.cuisine_type)

    def open_restaurant(self):
        print('the %s is open!' %self.restaurant_name)

    def set_number_served(self, number_served):
        # 禁止随便填写客户数量
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print('you input wrong customer number!')

    def increment_number_served(self, number_served):
        # 将用餐人数设置为指定的人数
        self.number_served += number_served

    def read_served(self):
        print('This restaurant has %s customers today' %self.number_served)


restaurant = Restaurant('KFC', 'western type')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.read_served()
restaurant.increment_number_served(10)
restaurant.read_served()
restaurant.set_number_served(9)
restaurant.read_served()
restaurant.set_number_served(11)
restaurant.read_served()

print('\n')

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print('this customer first name is %s, last name is %s' %(self.first_name, self.last_name))

    def greet_user(self):
        print('hello %s %s!' %(self.first_name, self.last_name))

    def increment_login_attempts(self, login_attempts):
        self.login_attempts += login_attempts

    def reset_login_attempts(self):
        if self.login_attempts != 0:
            self.login_attempts = 0

    def read_login_times(self):
        print('Today has %d login times!' %self.login_attempts)

user = User('Zhao', 'Wei')
user.describe_user()
user.greet_user()
user.read_login_times()
user.increment_login_attempts(2)
user.read_login_times()
user.reset_login_attempts()
user.read_login_times()
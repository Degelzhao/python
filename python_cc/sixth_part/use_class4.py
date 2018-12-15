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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['milk', 'herb', 'coffee']

    def dsp_ice_cream(self):
        for flavor in self.flavors:
            print('we have %s ice cream' % flavor)

my_ice_cream = IceCreamStand('KFC', 'ice_cream')
my_ice_cream.describe_restaurant()
my_ice_cream.dsp_ice_cream()
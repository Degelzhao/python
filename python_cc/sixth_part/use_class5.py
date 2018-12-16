class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('this administrator first name is %s, last name is %s' %(self.first_name, self.last_name))

    def greet_user(self):
        print('hello %s %s!' %(self.first_name, self.last_name))

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # 创建一个新的privilege实例，并将该实例存储在属性self.privilege中
        self.privilege = Privileges()


class Privileges():

    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
        # 初始化privileges的属性
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print('The administrator limit has: %s' %privilege)

admin = Admin('Zhao', 'Wei')
admin.describe_user()
admin.privilege.show_privileges()
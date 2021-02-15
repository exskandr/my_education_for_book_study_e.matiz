class Restaurant():
    """"simply class restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """initializes attribute name and type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """method for output two attribute"""
        print(f'Our restaurant {self.restaurant_name.title()} has '
              f'{self.cuisine_type} cuisine')

    def open_restaurant(self):
        """method open restaurant"""
        print(f'{self.restaurant_name.title()} is OPEN!!!')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['ice', 'cream']

    def describe_flavors(self):
        for self.flavor in self.flavors:
            print(self.flavor)
#
#
# my_ice = IceCreamStand("cosacs", "ukrainian")
# my_ice.describe_restaurant()
# my_ice.describe_flavors()
# my_restaurant = Restaurant('cosacs', 'ukrainian')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# print(my_restaurant.number_served)
# my_restaurant.number_served = 20
# print(my_restaurant.number_served)
# my_restaurant.set_number_served(5)
# print(my_restaurant.number_served)
# my_restaurant.increment_number_served(7)
# print(my_restaurant.number_served)

# print(my_restaurant.restaurant_name.title())
# print(my_restaurant.cuisine_type.upper())
# j_restaurant = Restaurant('jap', 'japanian')
# j_restaurant.describe_restaurant()
# ger_rest = Restaurant('shvaine', 'germania')
# ger_rest.describe_restaurant()

class User():
    """siply class user"""

    def __init__(self, first_name, last_name, age, sex):
        """initializes attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print(f'\nName: {self.first_name.title()}')
        print(f'Last Name: {self.last_name.title()}')
        print(f'Age: {str(self.age)}')
        print(f'Sex: {self.sex.title()}')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    def __init__(self):
        self.privileges = [
            'разрешено добавлять сообщения',
            'разрешено удалять пользователей',
            'разрешено банить пользователей'
        ]

    def show_privileges(self):
        for self.privilege in self.privileges:
            print(f'админу {self.privilege}')


class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(self, first_name, last_name, age)
        self.privileges = Privileges()
        # self.privileges = [
        #     'разрешено добавлять сообщения',
        #     'разрешено удалять пользователей',
        #     'разрешено банить пользователей'
        # ]

admin = Admin('adik', 'ad', 22, 'male')
admin.privileges.show_privileges()

# joy = Admin('joy', 'toner', 33, 'male')
# joy.show_privileges()
# sveta = User('sveta', 'soner', 23, 'female')
# stefan = User('stefan', 'pop', 31, 'male')
# stefan.describe_user()
# stefan.greet_user()
# sveta.describe_user()
# sveta.greet_user()
# sveta.increment_login_attempts()
# sveta.increment_login_attempts()
# sveta.increment_login_attempts()
# print(str(sveta.login_attempts))
# sveta.reset_login_attempts()
# print(sveta.login_attempts)
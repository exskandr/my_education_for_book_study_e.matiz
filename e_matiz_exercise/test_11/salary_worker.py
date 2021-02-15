import datetime


class Employee():
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.register_year = 2020
        self.salary_year = 5000

    def give_raise(self):
        d = datetime.datetime.now().year
        r = int(self.register_year)
        if d > r:
            experience = d - r
            self.salary = self.salary + self.salary_year * experience
            print(self.salary)
            return self.salary

    def show_employeer(self):
        name = self.firstname
        last = self.lastname
        employeer = f'{name} {last}: {self.salary}'
        print(employeer)
        return employeer


son = Employee('son', 'son', 2000)
son.salary = 1000
son.show_employeer()
son.give_raise()
son.show_employeer()
pop = Employee('pop', 'popular', 1000)
pop.salary_year = 375
pop.salary = 1000
pop.show_employeer()
pop.give_raise()
pop.show_employeer()
print(son.salary)


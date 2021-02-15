# from class9 import Restaurant, User, Privileges, Admin
#
#
# cafe = Restaurant('cosa', 'GB')
# cafe.open_restaurant()
#
# les = User('lesya', 'bor', 34, 'female')
# les.greet_user()


from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        # print(x)
        return x

die = Die(10)
# die.roll_die()
# die2 = Die(6)
# die2.roll_die()
a = 0
while True:
    if a<10:
        a+=1
        s = die.roll_die()
        print(f'{a} - {s}')
    else:
        break

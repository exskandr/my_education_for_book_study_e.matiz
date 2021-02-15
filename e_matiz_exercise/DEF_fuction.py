# def display_message(for_person):
#     """Easy display message"""
#     print(f'Hello, {for_person.title()}')
#
#
# display_message("johny")


# def favorite_book(book):
#     book = input('Введіть назву улюбленої книги: ')
#     print(f'{book.title()} is one of my favorite book!')
#
# favorite_book('')

# def make_shirt(size_shirt='50', txt='I love PYTHON'):
#     print(f'\nрозмір футболки: {size_shirt}')
#     print(f'З текстом: "{txt}"')
#
#
# make_shirt()
# make_shirt('42', 'PYTHON')

# def describe_city(city='Kyiv', country = 'Ukraine'):
#     print(f'{city.title()} is in {country.title()}')
#
#
# describe_city()
# describe_city(city='kharkov')
# describe_city(city='london', country='greate britan')

# def city_country(n_city, n_country):
#     position = n_city + ' ' + n_country
#     return position.title()
#
#
# f_position = city_country('kyiv', 'ukraine')
# print(f'Hello, {f_position}')

# def make_album(n_song, n_album, amount=''):
#     album = {'song': n_song, 'album': n_album}
#     if amount:
#         album['amount'] = amount
#     return album
#
#
# while True:
#     n_song = input('song: ')
#     if n_song == 'q':
#         break
#     n_album = input('album: ')
#     if n_album == 'q':
#         break
#     n_amount = input('amount: ')
#     s_album = make_album(n_song, n_album, n_amount)
#     print(s_album)

# def print_models(unprinted_designs, completed_models):
#     """
# Имитирует печать моделей, пока список не станет пустым.
# Каждая модель после печати перемещается в completed_models.
# """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
# # Имитация печати модели на 3D-принтере.
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     """Выводит информацию обо всех напечатанных моделях.
#         """
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
#
# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician.title())
#
#
# def make_greate(magicians, g_magician):
#     while magicians:
#         current_magician = magicians.pop()
#         g = 'Greate ' + current_magician
#         #print(f'Greate {current_magician}')
#         g_magician.append(g)
#
#
# def show_greate_magicians(g_magician):
#     for magician in g_magician:
#         print(magician)
#
#
# magis = ['mag1', 'mag2', 'mag3']
# g_magis = []
# show_magicians(magis)
# make_greate(magis[:], g_magis) # - [:] - заборона на змінювання списку, якщо немає [:] то можна
# show_greate_magicians(g_magis)
# print(magis)
# print(g_magis)

# def make_pizza(size, *toppings):
#     """Выводит описание пиццы."""
#     print("\nMaking a " + str(size) +
#     "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     """Строит словарь с информацией о пользователе."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)

def make_car(name, mark, **car_info):
    car_dict = {}
    car_dict['name'] = name
    car_dict['mark'] = mark
    for key, value in car_info.items():
        car_dict[key] = value
    return car_dict

car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)


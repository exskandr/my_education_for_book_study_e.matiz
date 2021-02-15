# people = {}
# people['first_name'] = 'Jon'
# people['last_name'] = 'Ser'
# people['age'] = '23'
# people['town'] = 'Kyiv'
# # print(people)
# # print(people['town'])
# # for value in people:
# #     print(value, people[value], sep=': ')
#
# for key, value in people.items():
#     print(key, value, sep=': ')

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# persons = ['sarah', 'ira', 'phil']
#
# for name in persons:
#     if name.lower() not in favorite_languages.keys():
#         print(f'{name}, please take our poll!')
#     else:
#         print(f'{name}, thank you, for our poll!')
# for name in sorted(favorite_languages.keys()): # сортіровка по значенню ключів
#     print(name.title())
# for language in set(favorite_languages.values()): # сортіровка по унікальних значеннях (set())
#     print(language.title())

# rivers = {
#     'dnipro': 'ukraine',
#     'nile': 'egypt',
#     'misisippi': 'america'
# }
# for river in rivers.keys():
#     print(river.title())
# for country in rivers.values():
#     print(country.title())

# aliens = []
# for alien_number in range(25):
#     new_alien = {'color': 'red', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[0:3]:
#     if alien['color'] == 'red':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#
# for alien in aliens[:5]:
#     print(alien)
# print('total number of aliens: ' + str(len(aliens)))

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         for language in languages:
#             print(f'\n{name.title()}’s favorite language is {language.title()}')
#     else:
#         print("\n" + name.title() + "'s favorite languages are:")
#         for language in languages:
#             print("\t" + language.title())


woker = {
    'name': 'jon',
    'age': '23'
}
student = {
    'name': 'lucy',
    'age': '21'
}
people = [woker, student]

for person in people:
    for key, value in person.items():
        print(key.title(), value.title(), sep=': ')

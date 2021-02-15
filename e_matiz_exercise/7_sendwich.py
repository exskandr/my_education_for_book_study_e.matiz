# sandwich_orders = ['sandwich_1', 'sandwich_2', 'sandwich_3']
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f'verifying sandwich: {current_sandwich.title()}')
#     finished_sandwiches.append(current_sandwich)
# print('\n I made your: ')
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

# sandwiches = ['sandwich', 'sandwich_1', 'sandwich', 'sandwich_3', 'sandwich_2']
# print(sandwiches)
#
# while 'sandwich' in sandwiches:
#     sandwiches.remove('sandwich')
#
# print(sandwiches)

responses = {}
# Установка флага продолжения опроса.
polling_active = True
while polling_active:
# Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Ответ сохраняется в словаре:
    responses[name] = response
# Проверка продолжения опроса.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Опрос завершен, вывести результаты.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} - would like to climb {response}.")
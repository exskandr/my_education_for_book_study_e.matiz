# alien_color = ['green', 'yellow', 'red']
# color = 'yellow'
# if color != 'green':
#     print('you get 10')
# else:
#     print('you get 5')

# if color == 'green':
#     print('5')
# elif color == 'yellow':
#     print('10')
# elif color == 'red':
#     print('15')

# favorite_fruits = ['banane', 'apple', 'ananas']
# fruits = ('apple', 'banane')
# for fruite in fruits:
#     if fruite in favorite_fruits:
#         print(f'You really like {fruite}!')

# users = []
# #user = "Sveta"
# # for user in users:
# #     if user.lower() != "admin":
# #         print(f'Hello {user.title()},thank you for logging in again.')
# #     else:
# #         print(f'Hello {user.title()}, would you like to see a status report?')
#
# if users:
#     for user in users:
#         pass
# else:
#     print('We need to find some users!')

# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# # exercise with number
# nums = (str(value) for value in range(1, 10))
# for num in nums:
#     if num == '1':
#         print(f'{num}st')
#     elif num == '2':
#         print(f'{num}nd')
#     elif num == '3':
#         print(f'{num}rd')
#     else:
#         print(f'{num}th')

# exercise with current user
current_users = ['admin', 'Vlad', 'DELL']
new_users = ['dell', 'john', 'vlad']
for user in new_users:
    if user.lower() not in (user.lower() for user in current_users):
        print(f'your name {user.title()} is correct')
    else:
        print(f'Sorry, but name {user.title()} is busy')

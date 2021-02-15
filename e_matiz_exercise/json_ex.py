import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        answer = input(f'Are your name {username}? YES/NO ').lower()
        if answer == 'yes' or answer == 'y':
            return username
        else:
            get_new_username()


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username.title(), f_obj)
        print(f"We'll remember you when you come back, {username.title()}!")
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    # else:
    #     username = get_new_username()
    #     print(f"We'll remember you when you come back, {username}!")


greet_user()


###  love NUMBER  ###
# def get_number():
#     file_json = 'file_text\\likenumber.json'
#     try:
#         with open(file_json) as numb_obj:
#             love_number = json.load(numb_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return love_number
#
#
# def enter_number():
#     like_number = input('enter your like number: ')
#     file_json = 'file_text\\likenumber.json'
#     with open(file_json, 'w') as numb_obj:
#         json.dump(like_number, numb_obj)
#     return like_number
#
#
# def said_love_number():
#     number = get_number()
#     if number:
#         print(f'I know your love number. It is {number}')
#     else:
#         number = enter_number()
#         print(f"We'll remember your love number ({number})!")
#
#
# said_love_number()
import os

# file_path = 'C:\\Users\\CHEIF\\Desktop\\ID telegram.txt'
file = 'file_text\\pi_million_digits.txt'
# with open('pi_digits.txt') as file_object:
with open(file) as file_object:
    #contents = file_object.read()
    # print(contents.rstrip())
    # for line in file_object:
    #     print(line.rstrip())

    lines = file_object.readlines()
    # # for line in lines:
    # #     print(line.rstrip())
    # pi_string = ''
    # for line in lines:
    #     pi_string += line.strip()
    # print(pi_string)
    # print(len(pi_string))

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()

    birthday = input("Enter your birthday, in the form mmddyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")
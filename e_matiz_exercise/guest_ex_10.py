file_name = 'file_text\\guest.txt'

with open(file_name, 'a') as great_guest:
    # while True:
    #     prompt = input('enter your name: ').title()
    #     if prompt != 'Q':
    #         message = f'Hello, {prompt}!\n'
    #         print(message)
    #         great_guest.write(message)
    #     else:
    #         break
    while True:
        prompt = input('Why do you like programming? \n').title()
        if prompt != 'Q':
            message = f'- {prompt}!\n'
            print(message)
            great_guest.write(message)
        else:
            break
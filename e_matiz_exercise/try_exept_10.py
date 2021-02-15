"""програма для додавання двох чисел"""

# while True:
#     a = input('enter first number: ')
#     if a == 'q':
#         break
#     b = input('enter second number: ')
#     if b == 'q':
#         break
#     try:
#         print(int(a) + int(b))
#     except ValueError:
#         msr = 'не правильно введені дані. \n'
#         msr += 'Замість чисел літери'
#         print(msr)


# def analiz_text(file):
#     file_ad = f'file_text\\{file}'
#     try:
#         with open(file_ad)as f_obj:
#             text_r = f_obj.read()
#     except FileNotFoundError:
#         pass
#         # msg = f'sorry, the file {file} not found!'
#         # print(msg)
#     else:
#         print(f'{file} - ok\n')
#         print(f'{text_r}')
#         c = text_r.lower().count('sasha')
#         print(c)
#
#
# files_text = ['guest.txt', 'ex.txt', 'id_telegram.txt']
# for file in files_text:
#     analiz_text(file)

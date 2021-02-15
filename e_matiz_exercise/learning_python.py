file = 'file_text\\learning_python.txt'

with open(file) as file_obj:
    lines = file_obj.readlines()
    # for line in lines:
    #     print(line.strip())

    py_string = ''
    for line in lines:
        py_string += line.replace('Python', 'C#')
    print(py_string)
    print(len(py_string))
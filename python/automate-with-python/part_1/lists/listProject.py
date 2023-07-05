def list_to_string(some_list):
    new_string = ''
    if some_list:
        if len(some_list) == 1:
            new_string = str(some_list[0])
        else:
            for i in range(len(some_list) - 2):
                new_string += str(some_list[i]) + ', '
            new_string += str(some_list[len(some_list) - 2]) + ' and ' + str(some_list[len(some_list) - 1])
    return new_string

idolos = ['rony','veiga','dudu', 'gomez', 'weverton']
bagres = ['navarro','atuesta', 'jailson', 'lopez']

list_to_string(bagres)
print(bagres)
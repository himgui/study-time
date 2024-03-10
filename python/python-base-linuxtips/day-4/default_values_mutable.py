
def add_to_list(value, list=None):
    if list is None:
        list = []
    list.append(value)
    return list

add_to_list(4)
add_to_list(5)
print(add_to_list(6))
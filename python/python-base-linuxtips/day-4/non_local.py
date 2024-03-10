counting = 0

def add_to_count():
    global counting
    counting +=1

    sub_count = 0

    def internal_func():
        global counting
        counting +=1

        nonlocal sub_count
        sub_count +=1

    internal_func()


add_to_count()
add_to_count()


print(counting)
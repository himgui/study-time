# *args will print any arguments used in the function.
# **kwargs (can also use **options) will print any new variable assigned in the function.

def function(*args, timeout=10, **kwargs):
    for item in args:
        print(item)

    print(kwargs)
    print(f"timeout {timeout}")

function("[]", 7, "Palmeiras", name="Abel")
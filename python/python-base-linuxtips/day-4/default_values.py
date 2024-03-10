import time

def print_name(name, surname="Veiga"):
    print(f"Your name is {name} {surname}")

print_name("Gui")


def connect(host, timeout=10):
    print(f"Connecting with the {host} server...")
    for i in range(1, timeout +1):
        time.sleep(1)
        print("." * 1)
    print("Failed to connect")    

connect("localserver")
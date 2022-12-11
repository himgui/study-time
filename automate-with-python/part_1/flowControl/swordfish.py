while True:
    print('Who are you?')
    name = input()
    if name != 'Dudu':
        continue
    print('Hello, Dudu. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
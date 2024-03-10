

names = ["Abel", "Dudu", "Veiga", "Gomez", "Ze Rafael", "Piquerez"]

print(list(map(lambda name: "Hello, you are " + name, names)))

# Calc

operation = input("Operation: [sum, mul, div, sub]:").strip()
n1 = input("n1: ").strip()
n2 = input("n2: ").strip()

operations = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

result = operations[operation](int(n1),int(n2))
print(f"The result is: {result}")
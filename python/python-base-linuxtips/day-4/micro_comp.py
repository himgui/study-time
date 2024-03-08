names = [
    "Rony",
    "Raphael",
    "Rios",
    "Dudu",
    "Denilson",
]

# TODO: Lambdas

def starts_with_b(text):
    return text[0].lower() == "R"

print(*list(filter(starts_with_b, names)))
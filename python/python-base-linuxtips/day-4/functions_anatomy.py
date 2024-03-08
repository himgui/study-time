
# function Signature
# Docstring


# Param is something we still don't know and it's in the parenthesis on every function.
def my_function(a, b, c):
    """
    This function knows the alphabet.

    :param a: Int number
    :param b: Int number
    :param c: Int number

    >>> my_function(1,2,3)
    6

    """
    result = a + b + c
    return result

# Parsing positional arguments
value = my_function(1,2,3)

# Parsing named arguments
value = my_function(a=1,b=2,c=3)

# Parsing mixed arguments
value = my_function(1, b=2,c=3)

print(value)

# -------------------------

def another_function(a, b, c):
    """
    This is a nice function.
    """
    # Tuple as returned value.
    return a * 2, b * 2, c * 2

another_value = another_function(1, 2, 4)
print(another_value)

# --------------------------

def sum(n1, n2):
    """
    It sums.
    """
    return n1 + n2

print(sum(99, 2000))

# Args in a sequence
args = (10, 20)
# print(sum(args[0], args[1]))
print(sum(*args))

# Dictionary Args
args = {"n2": 90, "n1": 110}
print(sum(n1=args["n1"], n2=args["n2"]))
print(sum(**args))
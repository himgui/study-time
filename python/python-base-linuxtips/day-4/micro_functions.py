"""
Functions examples:
f(x) = 5 * (x / 2)
"""

from math import sqrt

def f(x):
    result = 5 * (x / 2)
    return result

print(f(10))
print(f(10) == 25)

def print_in_lower(text):
    """ Procedure with no explicit return"""
    print(text.lower())
    # return None

print_in_lower("SAO PAULO")


def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2


    area = s * (s - a) * (s - b) * (s - c)
    return sqrt(area)

triangle_area = heron(3, 4, 5)
print(triangle_area)

triangles = [
    (3, 4, 5),
    (5, 12, 15)
]

for t in triangles:
    area = heron(*t)    
    print(f" The triangle area is: {area}")
"""
Pseudo-code - It won't work.
"""

__version__ = "0.1.0"
__author__ = "Gui"

import go, pickup, ask, has, eat, stay

# Pre setting data
today = "Monday"
time = 15
xmas = False
rain = True
cold = True
snow = True
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
holiday = ["Wednesday"]
opening_hours = {
    "week": 19,
    "weekend": 12    
}

# Algorithm
if today in holiday and not xmas:
    bakery_open = False
elif today not in week and time < opening_hours["weekend"]:
    bakery_open = True
elif today in week and time < opening_hours["week"]:
    bakery_open = True
else: 
    bakery_open = False

if bakery_open:
    if rain and not (cold or snow):
        pickup("umbrella")
        pickup("jacket")
        pickup("boots")
    elif rain and not cold:
        pickup("umbrella")
        pickup("water")
    elif rain:
        pickup("umbrella")

    go("bakery")
    if has("int bread") and has("baguete"):
        ask(6, "int bread")
        ask(6, "baguete")
    elif has("int bread") or has("baguete"):
        ask(12, "Any of the two")
    else:
        ask(6, "Any bread")
else: 
    stay("Home")
    eat("Pizza")
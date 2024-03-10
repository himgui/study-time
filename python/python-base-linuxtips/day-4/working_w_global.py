name = "Plim plim"


def myfunction():
    name = "Local"
    print("Global Local:", name)
    name = globals()["name"]
    print("Global Name:", name)

myfunction()
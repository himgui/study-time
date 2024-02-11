#!/usr/bin/env python3

"""
Prefix Calculator

Operations available:
sum -> +
sub -> -
mul -> *
div -> /

All results are saved in a log file (prefix.logs).

"""
__version__= "0.1.0"
__author__= "Guilherme"
__license__= "Unlicensed"

import sys
import os
from datetime import datetime



while True:

    arguments = sys.argv[1:]

    if not arguments:
        operation = input("operation type:")
        n1 = input("n1")
        n2 = input("n2")
        arguments = [operation, n1, n2]

    elif len(arguments) != 3:
        print("Number of Arguments is invalid.")
        print("E.g ´sum 5 5´ ")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", "div")
    if operation not in valid_operations:
        print("Operation type is not valid.")
        print(valid_operations)
        sys.exit(1)

    validate_nums = []
    for num in nums:
        # TODO: Use While loop + exceptions
        if not num.replace(".","").isdigit():
            print(f"Number is invalid {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num =int(num)
        validate_nums.append(num)

    try:
        n1, n2 = validate_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)

    #TODO: Function dictionary

    if operation == "sum":
        result = n1 + n2
    elif operation == "sub":
        result = n1 - n2
    elif operation == "mul":
        result = n1 * n2
    elif operation == "div":
        result = n1 / n2

    path = os.curdir
    filepath = os.path.join(path, "prefix.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER', 'anonymous')

    print(f"The result is {result}.")

    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {operation},{n1}, {n2} = {result}\n")
    except PermissionError as e:
        print(str(e))
        sys.exit(1)
    
    if input("Press Enter to continue or any key to exit."):
        break
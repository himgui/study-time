#!/usr/bin/env python3

"""
Create a booking system.
"""
__version__ = "0.1.0"

import os
import sys
import logging


booked = {}
try:
    for line in open("book.txt"):
        name, room_num, days = line.strip().split(",")
        booked[int(room_num)] = {
            "name": name,
            "days": days
        }
except FileNotFoundError:
    logging.error("Book File not founded!")
    sys.exit(1)

rooms = {}
try:
    for line in open("rooms.txt"):
        code, name, price = line.strip().split(",")
        rooms[int(code)] = {
            "name": name,
            "price": float(price), #TODO Decimal
            "available": False if int(code) in booked else True
        }
except FileNotFoundError:
    logging.error("File not founded!")
    sys.exit(1)

print("-------- BOOKING DA SHOPEE --------")
print("-" * 40)

if len(booked) == len(rooms):
    print("| NO ROOMS AVAILABLE | ❤️")
    sys.exit(1)
    
name = input("Type your name: ").strip()

for code, data in rooms.items():
    room_name = data["name"]
    price = data["price"]
    available = "❌" if not data['available'] else "🗝️"
    print(f"{code} - {room_name} - R${price} - {available}")

print("-" * 40)
try:
    room_num = int(input("Room Number: ").strip())
    if not rooms[room_num]["available"]:
        print(f"The room {room_num} is not available.")
        sys.exit(1)
except ValueError:
    logging.error("Invalid room number, type only digits")
    sys.exit(1)
except KeyError:
    print(f"The Room Number {room_num} does not exist.")
    sys.exit(1)

try:
    booking_days = int(input("For how long?").strip())
except ValueError:
    logging.error("Invalid number of days, type only digits")
    sys.exit(1)

room_name = rooms[room_num]["name"]
room_price = rooms[room_num]["price"]
room_available = rooms[room_num]["available"]
total_price = room_price * booking_days

with open("book.txt", "a") as file_:
    file_.write(f"{name},{room_num},{booking_days}")

print(f"Hey {name}, you selected the {room_name} - price will be R$ {total_price}")
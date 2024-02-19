#!/usr/bin/env python3

"""
Weather Alert based on user inputs.
"""

import logging
import sys
log = logging.Logger("ALERT")

print("Weather Alert Program")
print("-----------------------")

try:
    current_temp = float(input("Type the current weather: ").strip())
except ValueError: 
    log.error("Invalid Temp")
    sys.exit(1)

try:
    current_humidity = float(input("Type the current humidity: ").strip())
except ValueError: 
    log.error("Invalid Hum")
    sys.exit(1)

print("Current Temperature is", current_temp)
print("Current Humidity is", current_humidity)
print("-----------------------")

if current_temp > 45:
    print("ALERT: Extreme Hot")
    sys.exit(1)
elif current_temp * 3 >= current_humidity:
    print("ALERT: Hot Humidity")
    sys.exit(1)
elif current_temp > 10 and current_temp < 30:
    print("ALERT: Normal Weather")
    sys.exit(1)
elif current_temp < 0:
    print("ALERT: Extreme Cold")
    sys.exit(1)
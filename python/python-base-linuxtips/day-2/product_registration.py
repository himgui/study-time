#!/usr/bin/env python

"""
Register a product
"""
__version__ = "0.1.0"

product_name = "Pizza"
product_type = "Food"
product_flavor = "Cheese"
product_price = 38.99
product_width = 0.8
product_height = 12.1
product_in_stock = True
product_code = 666
product_codebar = None

buy = ("Gui", product_name, 3)
buy_total = buy[2] * product_price

print(
    f"The client {buy[0]} bought {buy[1]}" 
    f" and paid in total ${buy_total}")
#!/usr/bin/env python

"""
Register a product
"""
__version__ = "0.1.0"

product = {
    "product_name": "Pizza",
    "product_type": "Food",
    "product_flavor": "Cheese",
    "product_price": 38.99,
    "product_size": {
        "product_width": 0.8,
        "product_height": 12.1,
    },
    "product_in_stock": True,
    "product_code": 666,
    "product_codebar": None,
}

client = {"name": "Gui"}
buy = {
    "client": client,
    "product": product,
    "amount": 4
}

buy_total = buy['amount'] * buy['product']["product_price"]

print(
    f"The client {buy['client']['name']}" 
    f" bought {buy['product']['product_name']}" 
    f" and paid in total ${buy_total}"
)
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:57:30 2018

@author: deepen
"""

class Product():
    
    # Constructor for the class Product
    def __init__(self, bar_code, price, name, quantity, unit):
        self.bar_code = int(bar_code)
        self.price = float(price)
        self.name = name
        self.quantity = int(quantity)
        self.unit = unit

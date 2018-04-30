# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:06:19 2018

@author: anjan
"""

class CheckoutRegister():
    # constructor for class CheckoutRegister.
    def __init__(self, product_list):
        self.product_list = []
        # initialize total amount to 0
        self.total_amount = 0.0
        # initialize paid amount to 0
        self.paid_amount = 0.0
        
    # function to scan product item and carry out necessary function
    def scan_item(self, product):
        # add up price of scanned product item to total amount.
        self.total_amount += float(product.price)
        # add up product item to the product list of this particular instance.
        self.product_list.append(product)
    
    # function to receive payment from user.
    def make_payment(self, amount):
        # add amount received from customer to total amount paid by customer.
        self.paid_amount += float(amount)
    
    # function to calculate due amount to be paid by customer.
    def calculate_due_amount(self):
        return self.total_amount - self.paid_amount
    
    # function to calculate change
    def calculate_change(self):
        return self.paid_amount - self.total_amount
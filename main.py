# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:20:48 2018

@author: anjan
"""

from Product import Product
from CheckoutRegister import CheckoutRegister

# default data for the products or to say inventory.
initial_products = [
        {
                'name': 'Bread',
                'bar_code': 100,
                'price': 1.00,
                'quantity': 1,
                'unit': 'loaf'
        },
        {
                'name': 'Butter',
                'bar_code': 101,
                'price': 2.45,
                'quantity': 350,
                'unit': 'gm'
        },
        {
                'name': 'Chicken',
                'bar_code': 121,
                'price': 5.01,
                'quantity': 1,
                'unit': 'kg'
        },
        {
                'name': 'Apple',
                'bar_code': 104,
                'price': 2.45,
                'quantity': 500,
                'unit': 'gm'
        },
        {
                'name': 'Banana',
                'bar_code': 115,
                'price': 2.45,
                'quantity': 4,
                'unit': 'pcs'
        },
    ]
# function to initialize inventory of products available.
def initialize_data(initial_products):
    # initialize empty list for inventory products.
    inventory_products = []
    # initialize empty list for the barcodes of all available products. To make
    #easy to check whether barcode entered by user is available in inventory
    product_barcodes = []
    # loop through initial_data and add product to the list
    for product in initial_products:
        temp_product = Product(product['bar_code'], product['price'], product['name'], 
                               product['quantity'], product['unit'])
        # add product to the inventory product list.
        inventory_products.append(temp_product)
        # add barcode of product to a list to make verification of barcode easier.
        product_barcodes.append(product['bar_code'])
    return inventory_products, product_barcodes

# main function
def main():
    # retrieve initial inventory products and list of barcodes of products.
    inventory_products, product_barcodes = initialize_data(initial_products)
    next_customer = 'n'
    # continue through new customer service till user inputs n or N as input
    # data
    while next_customer == 'n':
        # instantiate object of CheckoutRegister class with empty data.
        checkout_register = CheckoutRegister([])
        # greet user
        print('----- Welcome to FedUni Checkout! -----')
        while True:
            # scan barcode from user.
            item_barcode = int(input('Please enter the barcode of your item: '))
            # verify if the barcode provided by user exists in the list of inventory products barcodes.
            if item_barcode in product_barcodes:
                # loop through the inventory products to determine required product.
                for product in inventory_products:
                    if item_barcode == product.bar_code:
                        # display details of the scanned product.
                        print('{}, {} {} - ${}'.format(product.name, 
                              product.quantity, product.unit, product.price))
                        checkout_register.scan_item(product)
            # if verification fails, inform user that wrong barcode has been provided.
            else:
                print('This product does not exist in our inventory.')
            # ask user to scan another product.
            continue_again = input('Would you like to scan another product? \
                                       (Y/N)').lower()
            # if input is y or Y continue scanning
            if continue_again == 'y':
                continue
            # else breakout of the loop
            else:
                break
        # continue to receive payment from customer till the due is cleared.
        while checkout_register.calculate_due_amount() > 0:
            # handle exception if customer provides other input rather than money.
            try:
                payment_amount = float(input('Payment due: ${}. \
                                             Please enter an amount to pay: '.format(
                                             checkout_register.calculate_due_amount())))
                # payment amount should not be less than 0, else customer is to
                #be informed that system does not accept negative amount
                if payment_amount > 0:
                    checkout_register.make_payment(payment_amount)
                else:
                    print('We don\'t accept negative money!')
            # if customer enters data other than numerical value, request 
            # customer to provide appropriate amount.
            except ValueError:
                print('Please enter proper amount to pay.')
        # initialize final output string
        output_string = '----- Final Receipt -----'
        # append scanned product details to the output string.
        for product in checkout_register.product_list:
            output_string += '\n{}, {} {}'.format(product.name, 
                                product.quantity, product.unit)
        # append total amount of the scanned products to the output string.
        output_string += '\nTotal amount due: ${}'.format(checkout_register.total_amount)
        # append amount provided by customer as payment to the output string.
        output_string += '\nAmount received: ${}'.format(checkout_register.paid_amount) 
        # append change amount to the output string
        output_string += '\nChange given: ${}'.format(checkout_register.calculate_change())
        output_string += '\n\n'
        # greet customer
        output_string += 'Thank you for shopping at FedUni!'
        # display whole output string
        print(output_string)
        # ask if another customer wants to proceed with checkout.
        next_customer = input('(N)ext customer, or (Q)uit? ')

# execution of main function.
if __name__ == "__main__":
    main()
    
    
    
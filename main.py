# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:20:48 2018

@author: anjan
"""

from Product import Product
from CheckoutRegister import CheckoutRegister

# default data for the products or to say inventory.
initial_product_name = ['Apple', 'Banana', 'Egg', 'Milk', 'Beer', 'Chicken', 
                        'Bread', 'Shoes', 'Books', 'Shirt', 'Pants', 'Pen', 
                        'Pencil' ]
initial_product_code = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 
                        111, 112, 113]
initial_product_price = [2.50, 1.99, 2, 0.90, 20.00, 3.00, 1.50, 10.00, 22.00, 
                         7.00, 10.00, 10.50, 5.00]
initial_product_unit = ['kg', 'kg', 'cage', 'ltr', 'each', 'kg', 'gram', 
                        'pairs', 'each', 'each', 'pairs', 'pack', 'pack']
initial_product_quantity = [ 1, 1, 12, 1, 1, 1, 650, 1, 1, 1, 1, 12, 12]
#
# function to initialize inventory of products available.
def initialize_data(initial_products):
    # initialize empty list for inventory products.
    inventory_products = []
    # initialize empty list for the barcodes of all available products. To make
    #easy to check whether barcode entered by user is available in inventory
    product_barcodes = []
    # loop through initial_data and add product to the list
    for product in range(len(initial_product_name)):
        print(product)
        temp_product = Product(initial_product_code[product],
                               initial_product_price[product],
                               initial_product_name[product],
                               initial_product_quantity[product],
                               initial_product_unit[product])
        inventory_products.append(temp_product)
        product_barcodes.append(initial_product_code[product])
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
        checkout_register.print_receipt()
        # initialize final output string
        #output_string = '----- Final Receipt -----'
        # append scanned product details to the output string.
        #for product in checkout_register.product_list:
        #    output_string += '\n{}, {} {}'.format(product.name, 
        #                        product.quantity, product.unit)
        # append total amount of the scanned products to the output string.
        #output_string += '\nTotal amount due: ${}'.format(checkout_register.total_amount)
        # append amount provided by customer as payment to the output string.
        #output_string += '\nAmount received: ${}'.format(checkout_register.paid_amount) 
        # append change amount to the output string
        #output_string += '\nChange given: ${}'.format(checkout_register.calculate_change())
        #output_string += '\n\n'
        # greet customer
        #output_string += 'Thank you for shopping at FedUni!'
        # display whole output string
        #print(output_string)
        # ask if another customer wants to proceed with checkout.
        next_customer = input('(N)ext customer, or (Q)uit? ')

# execution of main function.
if __name__ == "__main__":
    main()
    
    
    
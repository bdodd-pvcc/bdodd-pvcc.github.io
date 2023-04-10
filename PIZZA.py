# Name: Brady Dodd
# Prog Purpose: Palermo Pizza Receipt

import datetime

# define tax rate and pizza prices
SALES_TAX_RATE = 0.055
PIZZA_PRICES = {
    'S': 9.99,
    'M': 12.99,
    'L': 14.99,
    'X': 17.99
}

def main():
    another_order = True
    while another_order:
        pizza_size, num_pizza = get_user_data()
        pizza_cost, sales_tax, total = perform_calculations(pizza_size, num_pizza)
        display_results(pizza_size, num_pizza, pizza_cost, sales_tax, total)
        yesno = input("\nWould you like to make another order? (Y/N): ")
        if yesno.upper() != "Y":
            another_order = False

def get_user_data():
    pizza_size = input("Pizza slice size (S, M, L, X): ")
    num_pizza = int(input("Number of pizza slices: "))
    return pizza_size.upper(), num_pizza

def perform_calculations(pizza_size, num_pizza):
    pizza_cost = PIZZA_PRICES.get(pizza_size, 0) * num_pizza
    sales_tax = pizza_cost * SALES_TAX_RATE
    total = pizza_cost + sales_tax
    return pizza_cost, sales_tax, total

def display_results(pizza_size, num_pizza, pizza_cost, sales_tax, total):
    print('------------------------------------')
    print('********** PALERMO PIZZA ***********')
    print('**********  434-555-1234 ***********')
    print('------------------------------------')
    print(str(datetime.datetime.now()))
    print('------------------------------------')
    print('Number of pizzas          : ' + str(num_pizza))
    print('Pizza size                : ' + pizza_size)
    print('Pizza cost                : $' + format(pizza_cost, ',.2f'))
    print('Sales tax                 : $' + format(sales_tax, ',.2f'))
    print('Total                     : $' + format(total, ',.2f'))
    print('------------------------------------')
    print('SQUARE PIZZA SO WE DONT CUT CORNERS.')
    print('------------------------------------')

# call the main function to execute the program
main()

# CTI-110
# P3HW2 - Pizza Order
# TIRADO
# 4.29.22
# This program calculates how many pizzas are needed in a group, number of pizza per person, and the cost.
import math

num_students = int(input('How many students do you want to order pizza for? '))
pizza_per = float(input('Enter number of people per pizza (1.5, 2, or 3): '))
pizza_needed = 0
pizza_cost = 5
before_tax = 0
tax = 0.06
total_price = 0

if pizza_per == 1.5:
    pizza_needed = num_students / pizza_per # example 27 / 1.5
    before_tax = (pizza_needed * pizza_cost)# example 18 * 5
    tax_applied = before_tax * tax          # example 90 * 0.06
    total_price = before_tax + tax_applied  # example 90 + 5.4
    pizza_needed = math.ceil(pizza_needed)  # Total price of pizza
    print()
    print('----Pizza Order-------')
    print(f'Pizzas Needed :{pizza_needed}') # Shows how many pizzas are needed
    print(f'Price ${total_price}')         # Total price of pizza
    print('----------------------')

elif pizza_per == 2:
    pizza_needed = num_students / pizza_per # example 27 / 2
    before_tax = (pizza_needed * pizza_cost)# example 13.5 * 5
    tax_applied = before_tax * tax          # example 67.5 * 0.06
    total_price = before_tax + tax_applied  # example 67.5 + 4.05
    pizza_needed = math.ceil(pizza_needed)  # Total price of pizza
    print()
    print('----Pizza Order-------')
    print(f'Pizzas Needed :{pizza_needed}') # Shows how many pizzas are needed
    print(f'Price ${total_price}')        # Total price of pizza
    print('----------------------')

elif pizza_per == 3:
    pizza_needed = num_students / pizza_per # example 27 / 3
    before_tax = (pizza_needed * pizza_cost)# example 9 * 5
    tax_applied = before_tax * tax          # example 45 * 0.06
    total_price = before_tax + tax_applied  # example 45 + 2.7
    pizza_needed = math.ceil(pizza_needed)
    print()
    print('----Pizza Order-------')
    print(f'Pizzas Needed :{pizza_needed}') # Shows how many pizzas are needed
    print(f'Price ${total_price}')        # Total price of pizza
    print('----------------------')

else:                                       # Shows error when user enters a value other than 1.5, 2, or 3
    print()
    print('INVALID ENTRY!!!!')
    print('Should have entered 1.5, 2, or 3\n')
    print('Run Program again\n')

input('press any button to exit.')

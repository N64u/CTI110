# CTI-110
# P4HW2 - Pizza Order
# Ibrahim Tirado-Gafar
# 5.7.2022
#
# imports math from libary
import math

def main():
    # Ask for how many students
    num_students = float(input('How many students do you want to order pizza for?'))
    
    # Values set
    pizza_needed = 0
    pizza_cost = 5
    before_tax = 0
    tax = 0.06
    total_price = 0
    
    # Expected inputs
    per_list = [1.5,2.0,3.0]
    # How many per student

    pizza_per = float(input("How many students do you want to order pizza for?(1.5, 2, 3)"))
    # set run to true
    run = True
    # while run is true the program will remain
    while run == True:
        # if user doesnt match per_list it will keep asking for valid input
        while pizza_per not in per_list:
            print('\nINVALID ENTRY!!!!')
            user_per = float(input('Enter number of people per pizza again.(1.5, 2 or 3):'))
        # if user inputs 1.5    
        if pizza_per == 1.5:
            pizza_needed = num_students / pizza_per # example 27 / 1.5
            before_tax = (pizza_needed * pizza_cost)# example 18 * 5
            tax_applied = before_tax * tax          # example 90 * 0.06
            total_price = before_tax + tax_applied  # example 90 + 5.4
            pizza_needed = math.ceil(pizza_needed)  # Total price of pizza
            print()
            print('----Pizza Order-------')
            print(f'Number of Students :{num_students}')
            print(f'Pizzas Needed :{pizza_needed}') # Shows how many pizzas are needed
            print(f'Price ${total_price:.2f}')         # Total price of pizza
            print('----------------------')
        # if user inputs 2
        elif pizza_per == 2:
            pizza_needed = num_students / pizza_per # example 27 / 2
            before_tax = (pizza_needed * pizza_cost)# example 13.5 * 5
            tax_applied = before_tax * tax          # example 67.5 * 0.06
            total_price = before_tax + tax_applied  # example 67.5 + 4.05
            pizza_needed = math.ceil(pizza_needed)  # Total price of pizza
            print()
            print('----Pizza Order-------')
            print(f'Number of Students :{num_students}')
            print(f'Pizzas Needed :{pizza_needed}') # Shows how many pizzas are needed
            print(f'Price ${total_price:.2f}')        # Total price of pizza
            print('----------------------')
        # if user inputs 3
        elif pizza_per == 3:
            pizza_needed = num_students / pizza_per # example 27 / 3
            before_tax = (pizza_needed * pizza_cost)# example 9 * 5
            tax_applied = before_tax * tax          # example 45 * 0.06
            total_price = before_tax + tax_applied  # example 45 + 2.7
            pizza_needed = math.ceil(pizza_needed)
            print()
            print('----Pizza Order-------')
            print(f'Number of Students :{num_students}')
            print(f'Pizzas Needed :{pizza_needed}') # Shows how many pizzas are needed
            print(f'Price ${total_price:.2f}')        # Total price of pizza
            print('----------------------')
        # ask user if they want to run program again
        run = input('\nWant to run program again?(Y / N)')
        # if yes then the loop restarts
        if run == 'y':
            main()
main()

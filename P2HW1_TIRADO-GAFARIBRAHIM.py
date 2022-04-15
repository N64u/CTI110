#This program calculates your subtotal, sales tax, and total of 5 items
#4/15/2022
#CTI-110 P2HW1 - Total Purchases
#Ibrahim Tirado-Gafar
#
#FLOAT INPUT DISPLAY "Enter the price of item #1:"
item_price1 = float(input("Enter the price of the item #1:\n"))
#FLOAT INPUT DISPLAY "Enter the price of item #2:"
item_price2 = float(input("Enter the price of the item #2:\n"))
#FLOAT INPUT DISPLAY "Enter the price of item #3:"
item_price3 = float(input("Enter the price of the item #3:\n"))
#FLOAT INPUT DISPLAY "Enter the price of item #4:"
item_price4 = float(input("Enter the price of the item #4:\n"))
#FLOAT INPUT DISPLAY "Enter the price of item #5:"
item_price5 = float(input("Enter the price of the item #5:\n"))

#SET sales_tax to 7%
sales_tax = 0.07

#processing subtotal SUM of item_price1, item_price2, item_price3, item_price4, item_price5
subtotal = item_price1+item_price2+item_price3+item_price4+item_price5
sales_tax_total = subtotal*sales_tax
sales_total = subtotal+sales_tax_total

#DISPLAYS "_______Results_______"
print("_______Results_______\n")
#DISPLAYS "Subtotal" 
print("Subtotal:\t", end='')
#FLOATING POINTOUTPUT REDUCED TO 2 digits after the decimal
print(f'{subtotal:.2f}')
#DISPLAYS "Sales Tax"
print("Sales Tax:\t", end='')
#FLOATING POINTOUTPUT REDUCED TO 2 digits after the decimal
print(f'{sales_tax_total:.2f}')
#DISPLAYS "Total"
print("Total:\t", end='')
#FLOATING POINTOUTPUT REDUCED TO 2 digits after the decimal
print(f'{sales_total:.2f}')



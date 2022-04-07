# This program calculates the number of pizzas needed.
# 4/7/2022
# Ibrahim Tirado-Gafar
#
#INPUT DISPLAY "How many students do you want to order pizza for?
num_students = int(input("How many students do you want to order pizza for?")) #int converts string to int

# SET num_pizza_slices to 6
num_pizza_slices = 6
# SET per_students to 3
per_students = 3
#processing
total_pizza = num_students*per_students/num_pizza_slices   # Multiplies then divides inputs

total_pizza_slices = num_students*per_students             # Multiplies both inputs
#ROUND total_pizza_rounded
total_pizza_rounded = round(total_pizza)                   # Rounds to the nearest whole
#output
print()
# DISPLAY "----Pizza Order--------"
print("----Pizza Order--------")
# DISPLAY "Pizza of Students :" +num_students
print("Number of Students :", num_students)
# DISPLAY "Pizza Slices Needed :" + total_pizza_slides
print("Pizza Slices Needed:", total_pizza_slices)
# DISPLAY "Pizza Needed :" + total_pizza
print("Pizzas Needed :", total_pizza)
# DISPLAY "Pizzas Needed(Rounded?)" + total_pizza_rounded
print("Pizzas Needed(Rounded?) :", total_pizza_rounded)
# DISPLAY "-----------------------"
print("-----------------------")

# This program calculates the users scores to find their grade using the 10 point grading scale.
# 5.8.22
# CTI-110 P5HW1 - Score List
# Ibrahim Tirado-Gafar
#

# user_range = int(input('How many scores do you want to enter?'))
score_list = []
user_score =  0
user_range = 0
set_range = 0
# counts each loop

i = 1

# 10 point grade scale    
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 59

# Main Function
def main():

    # Default choice
    choice = 0    

    # Function to find user's range, then ask for the scores from the user, also detects invalid inputs if under 0 or over 100
def set_range(user_range):
    global i
    user_range = int(input("Enter how many scores do you want to enter?"))
    score_list = []
    for user_score in range(user_range):
        
        
        user_score = int(input(f'Enter score #{i}:'))
        score_list.append(user_score)
        i += 1
        if user_score < 0 or user_score > 101:
            i -= 1
            score_list.remove(user_score)
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            user_score = int(input(f'Enter score#{i} again:'))
            i += 1
            
    # Returns the list from the user's inputs
    return score_list
    
    #function to find the lowest score in the list
def min_score(score_list):
    print('\n----------Result----------')
    print(score_list)
        # Finds the lowest score in the list
    min_score = min(score_list)
    print(f'Lowest Score  : {min_score}')
        # function to remove the lowest score from the list
def remove_min_score(score_list):    
        # removes the lowest score
    score_list.remove(min(score_list))
    print(f'Modified List : {score_list}')
        #functuon to find the average of the list
def avg_score(score_list):
    # Finds the average in the list
    global avg_user_score
    avg_user_score = sum(score_list)/len(score_list)
    print(f'Score Average : {avg_user_score:.2f}') 
    return avg_user_score

    # function to find the grade letter using the average and computing the averages for each grade letter. ie 90 = Grade    : A.
def grade_scale (avg_user_score):
    if (avg_user_score >= A_score) and not (user_score >100):       #min 90 max 100
        print('Grade         : A.')
        print('--------------------------')
            
    elif (avg_user_score >= B_score) and not (user_score > 100):    #min 80 max 89
        print('Grade         : B.')
        print('--------------------------')
            
    elif(avg_user_score >= C_score) and not (user_score > 100):     #min 70 max 79
        print('Grade         : C.')
        print('--------------------------')
            
    elif(avg_user_score >= D_score) and not (user_score > 100):     #min 60 max 69
        print('Grade         : D.')
        print('--------------------------')
            
    elif(avg_user_score <= F_score) and not (user_score > 100):     #max 59
        print('Grade         : F.')
        print('--------------------------')
# function for main menu
def print_menu():
    print('MAIN MENU')
    print('   1.) Create Score List')
    print('   2.) Display Results')
    print('   3.) Exit.')
  # default 0
choice = 0
# while user's choice is not 3, program will remain
while choice != 3:
    print_menu()
    choice = int(input('Enter choice: '))
    if choice == 3 :
        print('Goodbye.')
        
        
    else:
        # if user choice is 1 it will run the first function to ask the user's range and score
        if choice == 1:
            score_list = set_range(user_range)
            # if user choice is 2 it will run the following functions to show the results
        elif choice == 2:
            min_score(score_list)
            remove_min_score(score_list)
            avg_score(score_list)
            grade_scale(avg_score(score_list))
        print()
    
            
main()                         


# CTI-110
# P4HW1 - Score List
# Ibrahim Tirado-Gafar
# 5.7.2022
#

def main():
# Ask user to set range
    user_range = int(input('How many scores do you want to enter?'))
    score_list = []
    user_score =  0
# counts each loop    
    i = 1
# 10 point grade scale    
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59

    # limits range by user's input
    for user_score in range(user_range):
        user_score = int(input(f'Enter score #{i}:'))
        # Counts each increment by 1
        i += 1

        # if user inputs a score under 0 or over 100
        while user_score < 0 or user_score > 101:
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            user_score = int(input(f'Enter score #{i} again:'))
        # Updates list with user's score    
        score_list.append(user_score)
    print('\n----------Result---------')
    # Finds the lowest score in the list
    print(f'Lowest Score  : {min(score_list)}')
    # removes the lowest score
    score_list.remove(min(score_list))
    print(f'Modified List : {score_list}')
    # Finds the average in the list
    print(f'Score Average : {sum(score_list)/len(score_list):.2f}')
    # Branches to find user's grade
    
    if (user_score >= A_score) and not (user_score >100): #min 90 max 100
        print('Grade         : A.')
        
    elif (user_score >= B_score) and not (user_score > 100): #min 80 max 89
        print('Grade         : B.')
    
    elif (user_score >= C_score) and not (user_score > 100): #min 70 max 79
        print('Grade         : C.')
    
    elif (user_score >= D_score) and not (user_score > 100): #min 60 max 69
        print('Grade         : D.')
        
    elif (user_score <= F_score) and not (user_score > 100): #max 59
        print('Grade         : F.')

main()

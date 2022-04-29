# This program calculates your grade using the 10 point grade-scale.
# 4/29/2022
# CTI-110 P3HW1 - Debugging
# Tirado-Gafar

def main():
    #10 point grade-scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59

    score = int(input('Enter grade: '))
    
    if (score >= A_score) and not (score >100): #min 90 max 100
        print('Your grade is: A.')
        
    elif (score >= B_score) and not (score > 100): #min 80 max 89
        print('Your grade is: B.')
    
    elif (score >= C_score) and not (score > 100): #min 70 max 79
        print('Your grade is: C.')
    
    elif (score >= D_score) and not (score > 100): #min 60 max 69
        print('Your grade is: D.')
        
    elif (score <= F_score) and not (score > 100): #max 59
        print('Your grade is: F.')
        

main()

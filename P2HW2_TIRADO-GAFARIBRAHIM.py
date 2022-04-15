#CTI-110
#P2HW2 - Score Avg
#Ibrahim Tirado-Gafar
#4/15/2022
#
#DISPLAY FLOAT INPUT "ENTER SCORE #"
score1 = float(input("Enter score #1: "))
score2 = float(input("Enter score #2: "))
score3 = float(input("Enter score #3: "))
score4 = float(input("Enter score #4: "))
score5 = float(input("Enter score #5: "))
score6 = float(input("Enter score #6: "))
score7 = float(input("Enter score #7: "))

#List of scores
score_list = [score1,score2,score3,score4,score5,score6,score7]

#Space
print()
print()

#DISPLAY "--------------Results--------------"
print("--------------Results--------------")

#Finding min, avg, passing scores
print('Lowest Score  :',min(score_list))
#REMOVE min score from list
score_list.remove(min(score_list))
print('Modified List :',score_list)
print(f'Score Average: {sum(score_list)/len(score_list):.2f}')

#DISPLAYS "----------------------------------"
print("-----------------------------------")

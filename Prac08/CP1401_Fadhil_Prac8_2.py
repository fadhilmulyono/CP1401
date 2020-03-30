'''
Write a program that asks the user to enter 5 test scores.
The program should display a letter grade for each score and the average test score.
You will need to write the following functions, as well as main: 

calcAverage
The function should accept 5 test scores as arguments (or one array) and return the average of the scores

determineGrade
The function should accept a test score as an argument and return a letter grade for the score based on the grading scale below:

85-100	HD
75-84	D
65-74 	C
50-64	P
<50 	F

'''
def main():
    score1 = float(input("Enter Test 1 score: "))
    score2 = float(input("Enter Test 2 score: "))
    score3 = float(input("Enter Test 3 score: "))
    score4 = float(input("Enter Test 4 score: "))
    score5 = float(input("Enter Test 5 score: "))
    determineGrade(score1, score2, score3, score4, score5)
    calcAverage(score1, score2, score3, score4, score5)

def calcAverage(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    print ("The average score is: " + str(average))

def determineGrade(score1, score2, score3, score4, score5):
    if score1 < 50:
        grade1 = "F"
    elif score1 >= 50 and score1 < 65:
        grade1 = "P" 
    elif score1 >= 65 and score1 < 75:
        grade1 = "C" 
    elif score1 >= 75 and score1 < 85:
        grade1 = "D" 
    elif score1 >= 85 and score1 <= 100:
        grade1 = "HD" 
    
    if score2 < 50:
        grade2 = "F"
    elif score2 >= 50 and score2 < 65:
        grade2 = "P" 
    elif score2 >= 65 and score2 < 75:
        grade2 = "C" 
    elif score2 >= 75 and score2 < 85:
        grade2 = "D" 
    elif score2 >= 85 and score2 <= 100:
        grade2 = "HD" 
    
    if score3 < 50:
        grade3 = "F"
    elif score3 >= 50 and score3 < 65:
        grade3 = "P" 
    elif score3 >= 65 and score3 < 75:
        grade3 = "C" 
    elif score3 >= 75 and score3 < 85:
        grade3 = "D" 
    elif score3 >= 85 and score3 <= 100:
        grade3 = "HD" 
    
    if score4 < 50:
        grade4 = "F"
    elif score4 >= 50 and score4 < 65:
        grade4 = "P" 
    elif score4 >= 65 and score4 < 75:
        grade4 = "C" 
    elif score4 >= 75 and score4 < 85:
        grade4 = "D" 
    elif score4 >= 85 and score4 <= 100:
        grade4 = "HD" 
    
    if score5 < 50:
        grade5 = "F"
    elif score5 >= 50 and score5 < 65:
        grade5 = "P" 
    elif score5 >= 65 and score5 < 75:
        grade5 = "C" 
    elif score5 >= 75 and score5 < 85:
        grade5 = "D" 
    elif score5 >= 85 and score5 <= 100:
        grade5 = "HD" 

    print ("Your Test 1 score is: " + str(score1) + " (" + grade1 + ")")
    print ("Your Test 2 score is: " + str(score2) + " (" + grade2 + ")")
    print ("Your Test 3 score is: " + str(score3) + " (" + grade3 + ")")
    print ("Your Test 4 score is: " + str(score4) + " (" + grade4 + ")")
    print ("Your Test 5 score is: " + str(score5) + " (" + grade5 + ")")

main()
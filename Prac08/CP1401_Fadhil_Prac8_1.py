'''
The government is considering extending the minimum retirement age (the age at which you can receive the age pension) to 70 years old. 
Write a program that will get name, birth month and birth year information for two different people. 
Your main function should call a second function calcRetirement that will take the birth year of a person and returns the year they will be eligible for the pension. 
Output the information for both users in a single statement.

For example the output would be:
“James will become eligible in May of 2067 and Marie will become eligible in September of 2064”
'''
def main():
    name1 = input("Enter your name: ")
    month1 = input("Enter your birth month: ")
    year1 = int(input("Enter your birth year: "))
    name2 = input("Enter your name: ")
    month2 = input("Enter your birth month: ")
    year2 = int(input("Enter your birth year: "))
    calcRetirement(name1, month1, year1, name2, month2, year2)

def calcRetirement(name1, month1, year1, name2, month2, year2):
    year3 = year1 + 70
    year4 = year2 + 70
    print(name1 + " will become eligible in " + month1 + " of " + str(year3) + " and " + name2 + " will become eligible in " + month2 + " of " + str(year4))

main()
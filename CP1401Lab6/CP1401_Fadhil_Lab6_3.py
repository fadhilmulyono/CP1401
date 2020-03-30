'''
A restaurant is offering meals at 50% discount. Write a program that reads in the cost of the meal and displays a receipt. An example is as follows:
Enter meal amount ($): 120
Receipt
Cost of meal: $120
50% discount: $60.0
Total amount: $60.0
'''

def main():
    meal = float (input("Enter meal amount ($): "))
    print("Receipt")
    disc = meal / 2
    print("Cost of meal: $" + str(meal))
    print("50% discount: $" + str(disc))
    print("Total amount: $" + str(disc))

main()
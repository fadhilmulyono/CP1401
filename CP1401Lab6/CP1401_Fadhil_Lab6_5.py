'''
The formula to compute the total amount, compounded with interest, for a loan L at the end of n years at i % interest per annum is as follows:
A = L(1+i/100)^n
Write a program that prompts user for 3 input - loan amount(L), duration in years(n) and interest rate in percent (i). The program computes and displays the final total based on the formula above. Example,
Enter loan amount: 1000
Enter duration: 3
Enter interest rate (%): 3
Total is $1092.73
'''

def main():
    L = float (input("Enter loan amount ($): "))
    n = int (input("Enter duration (years): "))
    i = float (input("Enter interest rate (%): "))
    A = L * (1 + i/100) ** n
    print("Total is $" + str(A))

main()
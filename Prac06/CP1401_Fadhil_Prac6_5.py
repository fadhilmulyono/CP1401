'''
Design and write a function to calculate a person’s pay for a variable number of hours worked. 
●	Create a constant called HOURLY_RATE set to 24.95
●	To Consider - should this be local to the function or global?
●	Ask the user to enter their number of hours worked. 
Remember to always use meaningful variable names for variables!
●	Then calculate and return their total pay

Add code to main which will call this function, and display their pay.
'''
HOURLY_RATE = 24.95

def calculatePay(hours):
    pay = hours * HOURLY_RATE
    return pay

def main():
    hours = int(input("How many hours you have worked? "))
    pay = calculatePay(hours)
    print("Your total pay is ${:.2f}".format(pay))

main()
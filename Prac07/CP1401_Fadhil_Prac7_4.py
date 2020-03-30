'''
Johnny has been told to write out his times tables, but he would rather code them instead.
Write code that will generate the times table for whatever integer is passed into the function.
The program should calculate the times tables for all numbers from 1 to 10 inclusive.
The output of the program when called with 5 should be similar to that below. 

Johnny's time tables
The times table for 5 is:
5 x 1 = 5  
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

All output should be displayed together in a single output
(which you can either display in the function, or in main when you call the function).
'''

def main():
    x = int(input("Enter a number: "))
    y = 1
    times = x * y
    print("Johnny's times table")
    print("The times table for " + str(x) + " is:")
    while y > 0:
        print(str(x) + " x " + str(y) + " = " + str(times))
        if y == 10:
            break
        y = y + 1
        times = x * y

main()
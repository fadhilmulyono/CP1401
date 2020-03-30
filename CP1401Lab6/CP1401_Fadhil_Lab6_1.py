# Write a program that accepts 3 numbers using the input function and displays the sum and average of these 3 numbers.

def main():
    numOne = float (input("Enter the first number: "))
    numTwo = float (input("Enter the second number: "))
    numThree = float (input("Enter the third number: "))
    sum = numOne + numTwo + numThree
    average = sum / 3
    print ("The sum is: " + str(sum))
    print ("The average is: " + str(average))

main()

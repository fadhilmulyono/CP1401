'''
Write a program that will display all numbers from 1 to 50 on separate lines. 
For numbers that are divisible by 3 print "Fizz" instead of the number. 
For numbers divisible by 5 print the word "Buzz". 
For numbers that are divisible by both 3 and 5 print "FizzBuzz". 
'''

def main():
    number = 0

    while number < 50:
        number += 1
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

main()
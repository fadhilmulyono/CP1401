'''
Before starting this task, you will need to learn something about string manipulation. 
This term means to obtain a string, and do something to it. 

One important piece of information to obtain from a string is its length. 
We can find that using the len(string) function.

For example:
name = ‘JoeBloggs'
length = len(name)
At this point, length now contains the integer value of 9

Sometimes we may want to obtain a series of characters from within the string. 
This series is called a “substring”. 
Let’s look at the variable name from above. 
In Python it is stored as:

0	1	2	3	4	5	6	7	8
j	o	e	b	l	O	g	g	s

Each of the numbers indicates the position in the string where the letter is located. 
We can tell Python to give us the values from a range of locations in the string by using the code below.

firstName = name[0:3]
lastName = name[3:9]

Write a small program that gets a sentence from the user and displays it, putting half of the phrase on each line.
You will need to use the len function.
Ensure you have 20 asterisks on the first line (use a loop), then the first half of the message.
Put the second half of the sentence on the next line, and put 20 more asterisks at the bottom of the output.
Also ensure you have error checking to make sure that the user entered a message.

********************
A stitch in time saves nine
********************

Suggested functions:

The functions main and getAsterisks should be straight forward, but we have given you the pseudocode for the dividePhrase to help you out.    

•	main -  concatenates a string and outputs it
•	getAsterisks (number) – returns a string containing the requested number of asterisks
•	dividePhrase (phrase) – splits the phrase appropriately, and returns a string containing both parts joined by a new line character

Function dividePhrase (phrase)
	You will need a variable to store the length of the string
	Set length to what's returned from calling len with the phrase passed in
	Set halfLength = length / 2 
	Make a substring containing the left half of the phrase (from 0 to halfLength)
	Make a substring containing the right half of the phrase (from halfLength to length)
	set a string variable to be leftHalf +  ‘\n’ + rightHalf
	Return the divided string to main
End Function
'''

def getAsterisks(number):
    stars = number*"*"
    return stars

def dividePhrase(phrase):
    length = len(phrase)
    halfLength = length // 2
    leftHalf = phrase[0:halfLength]
    rightHalf = phrase[halfLength:len(phrase)]
    return leftHalf + "\n" + rightHalf

def main():
    phrase = input("Enter a phrase: ")
    number = int(input("How many asterisks? "))
    print (getAsterisks(number))
    print (dividePhrase(phrase))
    print (getAsterisks(number))

main()
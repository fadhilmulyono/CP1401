'''
Throughout this subject you have heard us discuss the concept of scope.
A simple definition of scope is:
Scope is the set of program instructions over which a variable exists, i.e. can be referred to. 
1.	Write a function named getValue, that will get an integer value from the user and save it in a variable called number. 
Then your function should use number to output the value. 
2.	Use the following main function print number. 
You will get an error. 
What causes this error? 
How does scope apply to this situation?
def main ():
    print (number)
main()
3.	Rewrite getValue() and main() so that it the value of number is accessible in main.
'''

def getValue(number):
    print (number)

def main():
    value = int (input("Enter a value: "))
    getValue(value)

main()
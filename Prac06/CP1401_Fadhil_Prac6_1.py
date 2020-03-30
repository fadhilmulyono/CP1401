'''
Below you are given the algorithm (in pseudocode) for two functions, main and doMath. Implement both in Python.

function main():
    get x from user
    get y from user
    call doMath(x,y)

function doMath(lhs, rhs):
    sum = lhs + rhs
    diff = lhs – rhs
    product = lhs x rhs
    quotient = lhs / rhs
    display sum, diff, product, and quotient

Test the code with some simple values.
'''

def main():
    x = float (input("Enter X: "))
    y = float (input("Enter Y: "))
    doMath(x,y)

def doMath(lhs, rhs):
    sum = lhs + rhs
    diff = lhs - rhs
    product = lhs * rhs
    quotient = lhs / rhs
    print ("The sum is "+str(sum))
    print ("The difference is "+str(diff))
    print ("The product is "+str(product))
    print ("The quotient is "+str(quotient))

main()


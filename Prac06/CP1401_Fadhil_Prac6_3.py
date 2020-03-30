'''
Create a function called formatCurrency which receives in a double as input (this function does NOT ask the user!) 
and returns a string containing the number with a $ in front of it, with 2 decimal places. 
(REMINDER: you can use google to find out how to format a number as a string in python 3. 
Try to learn about a function called format )  
'''

def formatCurrency():
    currency = float(input("Enter the currency value: "))
    return currency

def main():
    currency = formatCurrency()
    print("${:.2f}".format(currency))
main()
'''
The formula to convert temperature in Fahrenheit to centigrade is as follows:
c = (f-32)*5/9;
Write a program that has input in Fahrenheit and displays the temperature in Centigrade.
'''

def main():
    f = float (input("Enter the temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("The temperature in Celsius is: " + str(c) + " °C")

main()
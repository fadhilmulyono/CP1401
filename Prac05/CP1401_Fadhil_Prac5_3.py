'''
Get height
Get weight
Calculate BMI (BMI = weight/(height^2 ))
Show BMI
'''

def main():
    height = float(input("Enter your height (m): "))
    weight = float(input("Enter your weight (kg): "))
    BMI = weight / (height ** 2)
    print("Your BMI is " + str(BMI))

main()

'''
Implement the following flowchart as a new function in your Python project

getFuel(dist, fuelConsumption)
    fuelNeeded = dist * fuelConsumption / 100
    return fuelNeeded

Now add the following lines to main to test this function:
distance = 500
fuelCon = 8

fuel = getFuel(distance, fuelCon)
print(“Fuel needed is“, fuel)
'''

def getFuel(distance, fuelCon):
    fuel = distance * fuelCon / 100
    return fuel

def main():
    distance = 500
    fuelCon = 8
    fuel = getFuel(distance, fuelCon)
    print ("Fuel needed is "+ str(fuel))

main()

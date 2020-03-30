'''
Get houseCost
Get landSize
Get landCost
totalLandCost = landSize * landCost
totalCost = totalLandCost + houseCost
display totalLandCost
'''

def main():

    houseCost = int(input("Enter the cost of the house: "))
    #<WHAT ELSE DO WE GET FROM THE USER?>
    landSize = int(input("Enter the size of the land: "))
    landCost = int(input("Enter the cost of the land: "))

    totalLandCost = landSize * landCost
    #<HOW DO WE CALCULATE THE RESULT WE NEED?>
    totalCost = totalLandCost * houseCost

    print ("Total land cost: "+ str(totalLandCost))
    print ("Total cost: "+ str(totalCost))

main()

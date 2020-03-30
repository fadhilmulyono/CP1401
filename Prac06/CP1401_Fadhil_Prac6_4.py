'''
Design and write a function which will calculate and display the stock level of a product at the end of the day. 
The function will take as input the initial stock level, the amount we bought and the amount we sold.
'''

def calculateStock(initial, order, sold):
    print("Initial Stock Level: "+str(initial))
    print("Orders: +"+str(order))
    print("Sold: -"+str(sold))

def main():
    initial=int(input("Enter the product stock level: "))
    order=int(input("How many products are ordered? "))
    sold=int(input("How many products are sold? "))
    calculateStock(initial, order, sold)

main()
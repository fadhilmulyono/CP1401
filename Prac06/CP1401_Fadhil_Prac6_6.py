'''
Design and write a function that calculates and returns the discounted price of an item given a user’s input price and a fixed discount of 20%. 
Get the price from the user in main and pass it to the function. 
From main you need to call the function you created in Task Three to display the price.
'''
DISCOUNT = 20

def calculateDiscount(price):
    disc = price * DISCOUNT / 100
    sale = price - disc
    return sale

def main():
    price = float(input("Enter the price of the product: $"))
    sale = calculateDiscount(price)
    print ("Discounted price: ${:.2f}".format(sale))

main()
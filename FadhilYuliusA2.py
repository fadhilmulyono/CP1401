import sys #To allow the program to exit when the user request for quit

def main():
	print("Welcome to the Tropical Airlines Ticket Ordering System")
	print("Log in to the system using your username. A password is not required.")
	username = input("Username: ")
	get_username(username)
	#After login, show the welcome message, and then the menu options
	show_menu(username)
	#If any wrong input is made within the program, force the program to quit

def login(username):
	#Log in to the system using the username
	print("Welcome, " + username)
	#After login, show the welcome message, and then the menu options

def get_username(username):
	#Get username login details
	passenger = login(username)

def show_menu(username):
	#Show the menu options
	print ("\n")
	print ("----------- MENU ----------")
	print ("[I] nformation")
	print ("[O] rder ticket")
	print ("[E] xit")
	#Prompt the user to select the menu option by typing in the first letter of the options.
	menu = input("Type in the first letter of the menu option to select it: ")
	print ("\n")

	if menu == "I":
		#I = Display information message as detailed in information() function
		information()
	elif menu == "O":
		#O = Run through the ticket ordering process as detailed in order_ticket() function
		order_ticket(username)
	elif menu == "E":
		#E = Exit the program
		exit()
	else:
		#Display error message and force quit the program
		print("Unfortunately, the program has stopped.")
		sys.exit()

def information():
	print("Thank you for choosing Tropical Airlines for your air travel needs. You will be asked questions regarding what type of ticket you would like to purchase as well as destination information. We also offer 50% discounted fares for children.")
	show_menu()

def order_ticket(username):
	#Welcome to Ticket Ordering System
	print ("Welcome to the Ticket Ordering Wizard. Let's get you started.")

	print ("\n")
	print ("First of all, this is the ticket for:")
	print ("[Y] ou")
	print ("[S] omeone else")
	option = input("Type in the first letter of the option to select it: ")
	print ("\n")

	if option == "Y":
		#Declare the ticket for the user
		get_username(username)
		passenger = username
	elif option == "S":
		#Declare the ticket for another passenger. Ask to type in the name of passenger
		passenger = input ("Enter the name of passenger: ")
	else:
		print("Unfortunately, the program has stopped.")
		sys.exit()

	print("Dear " + str(passenger))

	#Ask user for the ticket type (single trip or return trip)
	print ("\n")
	print ("Is this a single trip or return trip ticket?")
	print ("[S] ingle trip - $100")
	print ("[R] eturn trip - $150")
	option = input("Type in the first letter of the option to select it: ")
	print ("\n")

	if option == "S":
		#Declare the ticket as single trip (one-way) ticket
		trip = "Single Trip"
		fare1 = 100
	elif option == "R":
		#Declare the ticket as return trip ticket
		trip = "Return Trip"
		fare1 = 150
	else:
		print("Unfortunately, the program has stopped.")
		sys.exit()
	
	#Ask user for the destination
	print ("\n")
	print ("Choose your destination.")
	print ("[C] airns - $125")
	print ("[S] ydney - $350")
	print ("[P] erth - $250")
	option = input("Type in the first letter of the option to select it: ")
	print ("\n")
	
	if option == "C":
		#Declare Cairns as their destination
		destination = "Cairns"
		fare2 = 125
	elif option == "S":
		#Declare Sydney as their destination
		destination = "Sydney"
		fare2 = 350
	elif option == "P":
		#Declare Perth as their destination
		destination = "Perth"
		fare2 = 250
	else:
		print("Unfortunately, the program has stopped.")
		sys.exit()

	#Ask user for flight class
	print ("\n")
	print ("Select your flight class.")
	print ("Seat choices are available for all classes except for the Frugal class.")
	print ("[F] rugal - Free")
	print ("[E] conomy - $50")
	print ("[B] usiness - $125")
	option = input("Type in the first letter of the option to select it: ")
	print ("\n")
	
	if option == "F":
		#Declare the flight as Frugal class
		flight = "Frugal Class"
		fare3 = 0
		#There are no seat choices for Frugal Class
	elif option == "E":
		#Declare the flight as Economy class
		flight = "Economy Class"
		fare3 = 50
	elif option == "B":
		#Declare the flight as Business class
		flight = "Business Class"
		fare3 = 125
	else:
		print("Unfortunately, the program has stopped.")
		sys.exit()

	#Ask the user for seat location unless the user chose the Frugal class
	print ("\n")
	if flight != "Frugal Class":
		print ("Select your seat location.")
		print ("[W] indow - $25")
		print ("[A] isle - $50")
		print ("[M] iddle - $75")
		option = input("Type in the first letter of the option to select it: ")
		print ("\n")
		
		if option == "W":
			#Declare the seat location close to the window
			seat = "Window"
			fare4 = 25
		elif option == "A":
			#Declare the seat location in the aisle
			seat = "Aisle"
			fare4 = 50
		elif option == "M":
			#Declare the seat location in the middle of the airplane
			seat = "Middle"
			fare4 = 75
		else:
			print("Unfortunately, the program has stopped.")
			sys.exit()
	else:
		#Automatically declare the seat location next to the window if the user chose the Frugal class
		print ("Because you chose the Frugal Class, you do not get to pick your seat choices.")
		seat = "Window"
		fare4 = 0

	#Get passenger age to calculate child's discount
	print ("\n")
	print ("We also offer a 50% child discount for passengers below 18 years old.")
	age = int(input("Enter the age of passenger and we will check your eligibility for a child discount: "))
	print ("\n")

	if age < 18:
		#If passenger's age is below 18 years old, get child discount
		discount = 2
		print ("Congratulations! You are eligible for a child discount.")
	else:
		discount = 1
		print ("Sorry, you are not eligible for a child discount.")
	
	#Calculate ticket prices formula
	price = (fare1 + fare2 + fare3 + fare4) / discount
	
	#Print the plane ticket order details
	print ("\n")
	print ("----------- ORDER DETAILS ----------")
	print ("Passenger Name: " + str(passenger))
	print ("Passenger Age: " + str(age))
	print (str(trip) + " Ticket")
	print ("Destination: " + str(destination))
	print ("Class: " + str(flight))
	print ("Seat: " + str(seat))
	print ("Ticket Price: ${:.2f}".format(price))
	print ("\n")

	#Prompt user to type in [Y] es to purchase another ticket or else quit
	print ("Will you order another plane ticket?")
	prompt = input("Type in [Y] es to order another plane ticket or anything else to log out from the system: ")

	if prompt == "Y":
		#Repeat the Order Ticket process
		print ("\n")
		order_ticket()
	else:
		#Display the Thank You message, show the order summary, and then quit
		print ("\n")
		print ("Thank you for using the Tropical Airlines Ticket Ordering System.")
		print ("Your ticket price is: ${:.2f}".format(price))
		print ("Your tickets will be emailed to you soon.")
		print ("Make sure you print your tickets and complete the payment as detailed in the Payment Instructions.")
		print ("Once you have printed your tickets and completed your payment, take them to the check-in counter at the airport!")
		print ("\n")
		sys.exit()


def exit():
	#Prompt user to type in [Q] uit to quit or else display the menu
	quit = input("Type in [Q] uit to log out from the system or anything else to display the menu again: ")
	if quit == "Q":
		#Display the Thank You message,  and then quit
		print ("Thank you for using the Tropical Airlines Ticket Ordering System.")
		print ("Unfortunately, you did not order or purchase any plane tickets!")
		print ("\n")
		sys.exit()
	else:
		show_menu()

main()
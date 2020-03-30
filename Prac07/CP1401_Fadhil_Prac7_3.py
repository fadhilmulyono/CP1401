'''
Below you are given the algorithm for two functions, main and printNames. Implement both in Python.

Function main():
	Make a list of size three that will hold first names
	Get 3 names from the user and store them in the list use a loop
	Call printNames, passing the list to the function

Function printNames (list):
	Get the length of the list
	Loop through the list, printing out each name and its location (0, 1, 2, etc)

Test the code with some simple values.
'''

def printNames(name):
    length = len(name)
    print("The length of the list is " + str(length))
    i = 0
    while i < length:
        print(i,name[i])
        i = i + 1

def main():
    name1 = input("Enter a name: ")
    name2 = input("Enter a name: ")
    name3 = input("Enter a name: ")
    list = [name1]
    list.append(name2)
    list.append(name3)
    printNames(list)

main()
'''
Part A
Write Python code that will get 5 values from a user and save them in a list. 
Once the list is filled the program should print the contents of the list.

Part B
Update the code from Part A to output the values from the list in ascending order.

You may find this code useful:
numbers = [3, 2, 8, 12, 11]
numbers.sort()

'''

def main():
    numbers = []
    new_number = int(input("Input a value: "))
    numbers.append(new_number)
    new_number = int(input("Input a value: "))
    numbers.append(new_number)
    new_number = int(input("Input a value: "))
    numbers.append(new_number)
    new_number = int(input("Input a value: "))
    numbers.append(new_number)
    new_number = int(input("Input a value: "))
    numbers.append(new_number)
    print("List (Part A)")
    print(numbers)
    numbers.sort()
    print("List after sorting (Part B)")
    print(numbers)

main()
'''
At a certain university, passwords for the university’s network must meet the following requirements:
•	Password must be at least 7 characters long

When a student creates a password it must be validated to ensure that it meets the criteria above. 
Write a program to display the criteria for the password, and ask for the password. 
Pass the password to a function that will evaluate whether the password is valid or not and return True or False to main. 
Then output a message to the user telling them whether their password has been accepted or that they must try again.
'''
def main():
    print("Create a new password to connect to the university's network systems.")
    print("The password must be at least 7 characters long.")
    while True:
        password = input("New password: ")
        if validatePassword(password):
            print("----- PASSWORD ACCEPTED -----")
            break
        else:
            print("The password you entered is too short.")

def validatePassword(password):
    if len(password) < 7:
        valid = "False"
    else:
        valid = "True"
    return valid

main()
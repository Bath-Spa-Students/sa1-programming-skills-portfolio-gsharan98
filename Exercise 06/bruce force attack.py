#Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
#1. Define the correct password.
#2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#3. Output an appropriate message when the correct password is entered.


def password_for_user_verification_system():        # asksing the user for accurate passcode and then checking if the passcode is correct
    accurate_passcode = "12345"                     # The accurate passcode for user verification
    
    while True:#this code is used to loop until the password input by the user is correct
        user_password = input("input the accurate passcode: ")#assigning a question to a variable for the user to input a password
        
        if user_password == accurate_passcode:
            print("the passcode is correct.!")            #it will print this output if the passcode is correct
            break#code that breaks the loop if answer given is correct 
        else:
            print("opps!incorrect answer,try again.")     #it will print this output , if the passcode is incorrect.

password_for_user_verification_system()




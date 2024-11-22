# Exercise 6: Brute Force Attack - 30 Marks

#Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

# Basic Requirements:
#1. Define the correct password.
#2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#3. Output an appropriate message when the correct password is entered.

#assgning a correct passcode,defining correct password
valid_passcode = "12345"

# amount of attempts a user can do
max_num_of_attempts = 3

# keeping track of how much attempts has been made from starting
attempts = 0

# this code is used to loop until the password input by the user is correct
while attempts < max_num_of_attempts:
    # asking user to input the passcode
    user_passcode = input(" enter the  correct passcode: ").strip() 
    
    # Masking  the entire password with asterisks for privacy reasons
    hidden_password = '*' * len(user_passcode)
    12
    
    # after every one incorrect answer increase the attempt
    #     attempts += 1

    # Checking if the inputed password matches the  user_passcode
    if user_passcode == valid_passcode:
        # If the answer is correct ,it will end loop instantly
        print("passcode is correct ,welcome")
        break
    else:
        # if thae answer is incorrect it will print wrong passcode
        print(f"wrong passcode: {hidden_password}")
        
        # giving hints if user is on their second to last attempts
        if attempts == max_num_of_attempts - 1:
            print("Hint: The password is an interger.")
        
        # after finishing of all the attempts they will be blocked
        if attempts == max_num_of_attempts:
            print("you have been blocked for a while.")

### Advanced Requirements:
#Have the user input their name, hometown, and age instead of hardcoding the values.
#Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
#Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?



# asking user to input their full name,  and removing extra whitespace

user_name = input(" Enter your full name: ").strip()            # .strip() function  helps to get rid of extra spaces around  the input

# asking the user to input their hometown,  and removing  extra whitespace

user_hometown = input("Enter your hometown: ").strip()          # .strip() function  helps to get rid of extra spaces around  the input

# asking the user to input their age in a loop ,it will keep looping until user input a valid answer.
while True:
    try:
        # Converting the input to an integer
        user_age = int(input("Enter your age: "))
        break                                       #  it will automatically break the loop if the conversion is successful
    except ValueError:
        #  assiging to print incorrect input, if input is not an interger
        print("Incorrect input. Please enter an interger value for age.")

# assigning to Display  all the  information collected.
print("\nUser Information:")
print(f"Name: {user_name}")
print(f"Hometown: {user_hometown}")
print(f"Age: {user_age}")



#Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
#1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#2. Input Handling: Ask the user to input the month number.
#3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.



# in dictionary, assgning each month number to number of daysin that month
days_in_month = {
    1: 31,   # January
    2: 28,   # February (assuming a non-leap year)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Asking  the user to input any month value
try:
    month_value = int(input("enter a month number (1-12): ").strip()) # .strip()  helps to get rid of extra spaces around input

    # Checking if the month value is within the valid range
    if month_value in days_in_month:
        # Displaying the number of days for the entered month
        print(f"The number of days in month {month_value} is {days_in_month[month_value]}.")
    else:
        #  printing this if the the input is out of the range.
        print("That's an invalid month number. Please input a number between 1 and 12.")

except ValueError:
    #  printing if the the input is not an interger
    print("Invalid input.make sure to enter a numerical value between 1 and 12.")

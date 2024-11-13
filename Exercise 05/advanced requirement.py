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
    month_value = int(input("enter the month number (1-12): ").strip())  # # .strip()  helps to get rid of extra spaces around input.

    # Checking if the entered month value is within the range of (1-12)
    if 1 <= month_value <= 12:
        
            #  for  (month 2) fenruary , we need to check for a leap year
        if month_value == 2:
            # Asking  the user if the year is a leap year
            leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
            # If it's the a leap year, February will have 29 days; else, it will have 28 days
            days = 29 if leap_year == "yes" else 28
        else:
            # For other months,it will be same from dictionary
            days = days_in_month[month_value]
        
            # Output the number of days in the selected month
        print(f"The number of days in month {month_value} is {days}.")
    else:
         #  printing this if the the input is out of the range.
        print("That's an invalid month number. Please input a number  from range between 1 and 12.")

except ValueError:
    #  printing if the the input is not an interger
    print("Invalid input.make sure to enter a numerical value between 1 and 12.")
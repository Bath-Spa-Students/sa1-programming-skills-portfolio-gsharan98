# a dictionary linking month number with number of days present in that month
the_days_in_month = {
    1: 31,   #here  January  is having 31 days
    2: 28,   # here February is having 28 days (considering it as leap year)
    3: 31,   # here March is having 31 days
    4: 30,   # here April is having 30 days
    5: 31,   # here May is having 31 days
    6: 30,   # here June is having 30 days
    7: 31,   # here July is having 31 days
    8: 31,   # here August is  having 31 days
    9: 30,   # here September is  having 30 days
    10: 31,  # here October is  having 31 days
    11: 30,  # here November is  having 30 days
    12: 31   # here December is having 31 days
}

# asking the user to input month number from 1- 12range
try:
    month_number = int(input("Please enter  month number with range (1-12): ").strip())  #  helps to eliminate extra spaces around input

    #checking if the month number is within the range
    if 1 <= month_number <= 12:
        
        # here we need to check for a leap year
        if month_number == 2:
            # asking user if its a leap year
            is_leap = input(" a leap year? (yes/no): ").strip().lower()
            # If it's a leap year, February will have 29 days; otherwise, it will have 28 days
            days = 29 if is_leap == "yes" else 28
        else:
            # same for other months
            days = the_days_in_month[month_number]
        
        # Output the number of days in the selected month
        print(f" number of days in month {month_number} is {days}.")
    else:
        # Inform the user if the month number is invalid (not between 1 and 12)
        print("thats not in range input from 1-12 range.")

except ValueError:
    # Handle cases where the user inputs something that isn't a number (e.g., text)
    print("thats invalid, eneter numerical value from 1-12")

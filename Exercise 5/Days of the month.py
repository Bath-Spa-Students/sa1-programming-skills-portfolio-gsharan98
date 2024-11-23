
#storing all the month number and days numbers in a dictionary
the_days_in_month = {
    1: 31,   # January
    2: 28,   # February (assuming  february as a non-leap year)
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

# asking the user to input any  month number  of their choice
try:
    month_number = int(input("Please enter any month number of your choice from 1-12: ").strip()) # .strip() helps to Removes the  extra spaces around input

    # checking if the given month is within range
    if month_number in the_days_in_month:
        # showing the number of days in month number
        print(f"The number of days in month {month_number} is {the_days_in_month[month_number]}.")
    else:
                                                                         
        print("thats invalid!please enter valid input within the range")  # it will display this output if its not a numerical value

except ValueError:
                                                             
    print("thats invalid, eneter numerical value from 1-12.")   # it will display this output if its not a numerical value
 

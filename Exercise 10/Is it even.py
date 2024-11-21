# checking if its odd or even by this function
def even_or_odd(number):
    # if we could evenly divide a number thats a even number
    if number % 2 == 0:
        return f"{number} is even."
    else:
        # If we can not evenly divide a number thats a odd number
        return f"{number} is odd."

# Main function to handle user input and display the result
def main():
    # asking the user to input a number
    try:
        user_number = int(input("enter a number: "))
         # Calling the check_even_odd function 
        result_message = even_or_odd(user_number)
         #  assigning to Printing  result message
        print(result_message)
    except ValueError:
        # if its a non interger value printing wrong answer
        print("not valid,please enter numerical value.")

#  assiging to Only run  main function if this script is running directly
if __name__ == "__main__":
    main()

#Loops- Pizza Toppings : 
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, 
#Print a message saying you’ll add that topping to their pizza.

#starting of a loop

print("Enter the toppings that you want on your pizza. Type 'finish' when you want to quit")

while True:
  toppings = input("Enter your toppings here:").strip().lower()            #("Enter your toppings here") this message will display ,as it will allow the user to input their topping that they want

  if toppings == 'finished':
    print("thank you for choosing us ! soon you will get your order.")    #if individual is finished with their toppinings they can say finished and message will display saying("thank you for choosing us ! soon you will get your order.")
    break
  else:
      print(f"we will be adding {toppings} to your pizza!")               #else it will continue adding toppings

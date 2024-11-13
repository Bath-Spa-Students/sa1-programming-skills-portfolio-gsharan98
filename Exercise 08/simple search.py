# Exercise 8: Simple Search - 30 Marks
#Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

#creating a list containing different strings
individual_names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#assiging searched_term as the variable for sam,as we want to search for sam
searched_term = "Sam"


#performing the search
if searched_term in individual_names:

    print("searched_term was found in the list.")

else:
     print ("searched_term ws not found in the list.")


### Optional Requirements:
#1. Allow the user to input the search term instead of using a predefined value.
#2. Implement the search functionality based on user input.

names =["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

searched_item = input("what you want to find in the list(Jake, Zac, Ian, Ron, Sam, Dave): ").lower()
print(type(names))
if searched_item == "Sam":
    searched_item = 4

elif  searched_item == "Zac":
    searched_item = 0

elif searched_item == "Ian":
    searched_item = 1

elif searched_item == "Ron":
    searched_item = 2

elif searched_item == "Sam":
    searched_item = 3

elif searched_item == "Dave":
    searched_item = 5

    print("you found",(names[searched_item])) 
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


#list of  avaible searched terms
names =["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]


# asking user to input the name they want to search for, using strip() to get rid of extra spaces
search_item = input("Please enter the name you want to search for: ").strip()

#  tracking if  the name is found during the search
found = False

# Loop through each name in the list to check if it matches the user's input
for name in names:
   
    # Converting  both names to lowercase to ensure the search is case-insensitive
    if name.lower() == search_item.lower():
       
        # if the searched item is  found, setting 'found' to True then we will let the user knoe
        found = True
        print(f"Great news! '{search_item}' is in the list.")
        break  # Exit the loop early since we found the name

# letting user know if loops complete and searched item is not found
if not found:
    print(f"Sorry, '{search_item}' is not  listed in the list.")
    

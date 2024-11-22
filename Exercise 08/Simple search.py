
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






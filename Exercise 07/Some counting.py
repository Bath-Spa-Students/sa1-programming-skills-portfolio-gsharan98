## Exercise 7: Some Counting - 20 Marks

#Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
#in each case.
# Write a loop that counts up from 0 to 50 in increments of 1.
 #Write a loop that counts down from 50 to 0 in decrements of 1.
 #Write a loop that counts up from 30 to 50 in increments of 1.
 #Write a loop that counts down from 50 to 10 in decrements of 2.
 #Write a loop that counts up from 100 to 200 in increments of 5.
 #You may include all loops in a single project*
 #Counting up from 0 to 50, one number at a time


print("Counting up from 0 to 50:")   #counting from 0 to 50 upwards
for i in range(0, 51, 1):
    print(i)

0
print("\nCounting down from 50 to 0:")  # counting from 50 to 0 ,downwards
for i in range(50, -1, -1):
    print(i)

# Counting up from 30 to 50, 
print("\nCounting up from 30 to 50:")   #counting from 30 to 50 ,downwards
for i in range(30, 51, 1):
    print(i)


print("\nCounting down from 50 to 10, skipping every other number:")   # counting downwards from 50 to 10 as we skip other numbers
for i in range(50, 9, -2):                      
    print(i)


print("\nCounting up from 100 to 200, adding 5 each time:")       #counting from 100 to 200, but we are adding 5 each time counts
for i in range(100, 201, 5):
    print(i)

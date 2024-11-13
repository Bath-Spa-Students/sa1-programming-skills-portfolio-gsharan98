### Steps:
#1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#2. Print the values on separate lines using a single `print()` statement.
#3. Use variables with appropriate data types for each piece of information.



# storing information in a  dictionary
name = "gursharan"              
hometown = "india"               
age = 18                        

# Storing  information in a dictionary with assigned  keys.
info = {
    "Name": name,                                        #  "Name" with the value of name
    "Hometown": hometown,                                #  "Hometown" with the value of hometown
    "Age": age                                           #  "Age" with the value of age
}

# assigning to print each information  on different lines.
print(f"{info['Name']}\n{info['Hometown']}\n{info['Age']}")

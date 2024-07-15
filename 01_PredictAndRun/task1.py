import re # Import python regex library

text = "This book on tennis cost $3.99 at Walmart." # Define the variable text with the string to search in

reg1 = re.compile("ten") # Define and compile the regular expression 'ten'
match = reg1.match(text) # Search for the regular expression at the beginning of the string stored in the variable text 
print(match) # Print the resulting match object

reg2 = re.compile("this") # Define and compile the regular expression 'this'
match = reg2.match(text) # Search for the regular expression at the beginning of the string stored in the variable text 
print(match) # Print the resulting match object

reg3 = re.compile("This") # Define and compile the regular expression 'This'
match = reg3.match(text) # Search for the regular expression at the beginning of the string stored in the variable text
print(match) # Print the resulting match object

match = reg1.search(text) # Search for the first occurrence of the regular expression anywhere in the string stored in the variable text
print(match) # Print the resulting match object

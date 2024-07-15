import re # Import python regex library

text = "This book on tennis cost $3.99 at Walmart." # Define the variable text with the string to search in

reg2 = re.compile("$This") # Define and compile the regular expression '$This' - $ means end of line
match = reg2.search(text) # Search for the first occurrence of the regular expression anywhere in the string stored in the variable text
print(match) # Print the resulting match object

reg2 = re.compile("^This") # Define and compile the regular expression '^This' - ^ means beginning of line
match = reg2.search(text) # Search for the first occurrence of the regular expression anywhere in the string stored in the variable text
print(match) # Print the resulting match object

reg2 = re.compile("This^")
match = reg2.search(text)
print(match)

reg2 = re.compile("This$")
match = reg2.search(text)
print(match)

reg2 = re.compile("Walmart\.$")
match = reg2.search(text)
print(match)


"""
Basic String Operations
"""

# 1. Strings can be defined as anything between quotes
astring = "Hello world!"
astring2 = 'Hello world!'

# 2. Use double quotes to avoid issues with apostrophes and single quotes
# len counts the characters including punctuation and spaces
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

# 3. index prints out 4, because the location of the first occurrence
# of the letter "o" is 4 characters away from the first character.
# this method only recognizes the first.
astring = "Hello world!"
print(astring.index("o"))

# 4. count counts the number of characters
astring = "Hello world!"
print(astring.count("l"))

# 5. slice of the string, starting at index 3, and ending at index 6
astring = "Hello world!"
print(astring[3:7])

# 6. [start:stop:step]
astring = "Hello world!"
print(astring[3:7:2])

# 7. reverse a string
astring = "0123456789"
print(astring[::-1])

# 8. upper and lower
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

# 9. startswith and endswith
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# 10. split
astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)

"""
YOU DO
5 minute timer
"""
# assign the string "Strings are awesome!" to a variable
str = "Strings are awesome!"

# print the length of the string
len(str)

# print the first occurrence of "a"
str.index('a')

# print the count of the number of "a"s in the string
str.count('a')

# print the first five characters
str[0:5] or 
str[:5]

# print the last five characters in reverse
newstr = str.[15:20]
newstr[::-1] or
print(str[:-6:-1])


# print the 17th character
str[16:17]
str[16]

# print all the odd indexes
print(str[1::2])

# print the string in all uppercase
str.upper()

# print the string in all lowercase
str.lower()

# check that the string starts with "S" and ends with "!"
str.startswith("S")
str.endsswith("S")

# split the string on the spaces
splitstr = str.split(" ")
    


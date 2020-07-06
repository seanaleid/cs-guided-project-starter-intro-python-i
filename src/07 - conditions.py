"""
Conditions
"""

# 1. Comparing or evaluating expressions
x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

# 2. "and" & "or"
name = "Sean"
age = 31
if name == "Matt" and age == 31:
    print("Your name is Matt, and you are also 31 years old.")
    # Does not evaluate the second conditional because it fails on the first one (name == 'Matt')
    # Like JS, both must be true.

if name == "Matt" or name == "Sean":
    print("Your name is either Matt or Sean.")
    # Prints because the first one fails, but the second one is true. Like JS only one has ot be true

# 3. "in"
my_name = "Beej"
names = ["Matt", "Sean"]
if my_name in names:
    print("Your name is either Matt or Sean.")

# 4. "if", "elif", "else"
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True:  # else if
    print("another statement is True")
    pass
else:
    # do another thing
    pass

# 5. "is" matches instances and not values
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False

# 6. "not" inverts a boolean
print(not False)  # Prints out True
print((not False) == (False))  # Prints out False


"""
YOU DO
3 minute timer
"""
# Modify the supplied code so that all of the statements evaluate to True
# change this code
number = 16
second_number = None
# second_number = 0 --> another original option
first_array = [1, 2, 3]
second_array = [1, 2]

print(bool(number > 15))

print(bool(first_array))

print(len(second_array) == 2)

print(len(first_array) + len(second_array) == 5)

print(first_array and first_array[0] == 1)

print(not second_number)

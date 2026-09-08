<<<<<<< HEAD
print("Hello, World!")

abcd= 23456
print(abcd)

# dont use the variable name as a keyword
# for example, dont use 'print' or 'input' as variable names
# some keywords are: if, else, for, while, def, class, return, import, from, as, with, try, except,
#  finally, raise, lambda, pass, break, continue, yield
# special characters are not allowed in variable names, except for the underscore (_)

a = 10
b = 20
c = 30
d = 40
print(a, b, c, d)

# data types in python are: int, float, str, bool, list, tuple, set, dict

a = 10 # int
b = 10.5 # float
c = "Hello" # str
d = True # bool
print(a, b, c, d)

a = [1, 2, 3, 4, 5] # list
b = (1, 2, 3, 4, 5) # tuple
print(a, b)

a = {1, 2, 3, 4, 5} # set
b = {"name": "John", "age": 30} # dict
print(a, b)

a = 10j # complex
print(a)

# type casting in python is done using the following functions: int(), float(), str(), bool(),
# list(), tuple(), set(), dict()

a ="10"
print(a)
print(type(a))

a = int(a)
print(a)
print(type(a))

a = float(a)
print(a)
print(type(a))

a = str(a)
print (a)
print(type(a))

a = bool(a)
print(a)
print(type(a))  


# Input in python is done using the input() function. The input() function takes a string as an argument and displays it to 
# the user. The user can then enter a value, which is returned as a string.

name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print("Your age is", age)

# Escape sequences in python are used to represent special characters in a string. The most common escape sequences are: \n, \t, \\, \', \", \r, \b, \f, \v

print("Hello\nWorld")  # New line
print("Hello\tWorld")  # Tab
print("Hello\\World")  # Backslash
print("Hello\'World")  # Single quote
print("Hello\"World")  # Double quote
print("Hello\rWorld")  # Carriage return
print("Hello\bWorld")  # Backspace
print("Hello\fWorld")  # Form feed
print("Hello\vWorld")  # Vertical tab

# Row strings in python are created using triple quotes. Row strings are used to represent multi-line strings.

a = """This is a multi-line string.
It spans multiple lines."""
print(a)

# A row string can also be created using single quotes or double quotes, but it is not recommended as it can lead to confusion.

a = 'This is a multi-line string.\nIt spans multiple lines.'
print(a)

a = "This is a multi-line string.\nIt spans multiple lines."
print(a)

a = '''This is a multi-line string.
It spans multiple lines.'''
print(a)

a = """This is a multi-line string.
It spans multiple lines."""
print(a)

a = r"This is a multi-line string.\nIt spans multiple lines."
print(a)

# Formatting strings in python is done using the format() method. The format() method takes a string as an argument and replaces the placeholders in the string with the values passed to the method.

name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("My name is {} and I am {} years old.".format(name, age))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")


#Arithmetic operators in python are: +, -, *, /, %, **, //

a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

#Comparison operators in python are: ==, !=, >, <, >=, <=

a = 10
b = 20
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)
print(a<b and a!=b)
print(a>b or a!=b)
print(not(a<b and a!=b))


# Control flow in python is done using the following statements: if, elif, else, for, while, break, continue, pass

a = 10
if a > 0:
    print("a is positive") 

a = -10
if a > 0:
    print("a is positive")
else:
    print("a is not positive")

age = int(input("Enter your age: "))
if age <= 18:
    print("You are a minor")
else:
    print("You are an adult")

item = input("Enter an item: ")
if item == "apple":
    print("You selected an apple")
elif item == "banana":
    print("You selected a banana")
else:
    print("You selected an unknown item")


# Range function in python is used to generate a sequence of numbers. The range() function takes three arguments: start, stop, and step. The start argument is the starting number of the sequence, the stop argument is the ending number of the sequence, and the step argument is the difference between each number in the sequence.

a = range(5)
print(a) # range(0, 5)

a = range(1, 10, 2)
print(a) # range(1, 10, 2)

# Converting range to a list
a = list(range(5))
print(a) # [0, 1, 2, 3, 4]

a = list(range(1, 10, 2))
print(a) # [1, 3, 5, 7, 9]

# Iterative statements in python are: for, while, break, continue, pass

# The for loop is used to iterate over a sequence (list, tuple, string, etc.)
for i in range(5):
    print(i)

for i in range(13, 150, 13):
    print(i)

for i in range(1,21,2):
    print(i)

for i in range(50,0,-2):
    print(i)


# The while loop is used to execute a block of code as long as a condition is true
i = 0
while i < 5:
    print(i)
    i += 1

i= 10
while i > 0:
    print(i)
    i -= 1



# The break statement is used to exit the loop
for i in range(5):
    if i == 3:
        break
    print(i)

a =20
while a > 0:
    if a == 10:
        break
    print(a)
    a -= 1


# The continue statement is used to skip the current iteration and move to the next iteration
for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(1,15):
    if i ==5 or i == 7:
        continue
    print(i)

# The pass statement is used as a placeholder when a statement is required syntactically but no action is needed
for i in range(5):
    if i == 3:
        pass
    print(i)
=======
print("Hello, World!")

abcd= 23456
print(abcd)

# dont use the variable name as a keyword
# for example, dont use 'print' or 'input' as variable names
# some keywords are: if, else, for, while, def, class, return, import, from, as, with, try, except,
#  finally, raise, lambda, pass, break, continue, yield
# special characters are not allowed in variable names, except for the underscore (_)

a = 10
b = 20
c = 30
d = 40
print(a, b, c, d)

# data types in python are: int, float, str, bool, list, tuple, set, dict

a = 10 # int
b = 10.5 # float
c = "Hello" # str
d = True # bool
print(a, b, c, d)

a = [1, 2, 3, 4, 5] # list
b = (1, 2, 3, 4, 5) # tuple
print(a, b)

a = {1, 2, 3, 4, 5} # set
b = {"name": "John", "age": 30} # dict
print(a, b)

a = 10j # complex
print(a)

# type casting in python is done using the following functions: int(), float(), str(), bool(),
# list(), tuple(), set(), dict()

a ="10"
print(a)
print(type(a))

a = int(a)
print(a)
print(type(a))

a = float(a)
print(a)
print(type(a))

a = str(a)
print (a)
print(type(a))

a = bool(a)
print(a)
print(type(a))  


# Input in python is done using the input() function. The input() function takes a string as an argument and displays it to 
# the user. The user can then enter a value, which is returned as a string.

name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print("Your age is", age)

# Escape sequences in python are used to represent special characters in a string. The most common escape sequences are: \n, \t, \\, \', \", \r, \b, \f, \v

print("Hello\nWorld")  # New line
print("Hello\tWorld")  # Tab
print("Hello\\World")  # Backslash
print("Hello\'World")  # Single quote
print("Hello\"World")  # Double quote
print("Hello\rWorld")  # Carriage return
print("Hello\bWorld")  # Backspace
print("Hello\fWorld")  # Form feed
print("Hello\vWorld")  # Vertical tab

# Row strings in python are created using triple quotes. Row strings are used to represent multi-line strings.

a = """This is a multi-line string.
It spans multiple lines."""
print(a)

# A row string can also be created using single quotes or double quotes, but it is not recommended as it can lead to confusion.

a = 'This is a multi-line string.\nIt spans multiple lines.'
print(a)

a = "This is a multi-line string.\nIt spans multiple lines."
print(a)

a = '''This is a multi-line string.
It spans multiple lines.'''
print(a)

a = """This is a multi-line string.
It spans multiple lines."""
print(a)

a = r"This is a multi-line string.\nIt spans multiple lines."
print(a)

# Formatting strings in python is done using the format() method. The format() method takes a string as an argument and replaces the placeholders in the string with the values passed to the method.

name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("My name is {} and I am {} years old.".format(name, age))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")


#Arithmetic operators in python are: +, -, *, /, %, **, //

a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

#Comparison operators in python are: ==, !=, >, <, >=, <=

a = 10
b = 20
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)
print(a<b and a!=b)
print(a>b or a!=b)
print(not(a<b and a!=b))


# Control flow in python is done using the following statements: if, elif, else, for, while, break, continue, pass

a = 10
if a > 0:
    print("a is positive") 

a = -10
if a > 0:
    print("a is positive")
else:
    print("a is not positive")

age = int(input("Enter your age: "))
if age <= 18:
    print("You are a minor")
else:
    print("You are an adult")

item = input("Enter an item: ")
if item == "apple":
    print("You selected an apple")
elif item == "banana":
    print("You selected a banana")
else:
    print("You selected an unknown item")


# Range function in python is used to generate a sequence of numbers. The range() function takes three arguments: start, stop, and step. The start argument is the starting number of the sequence, the stop argument is the ending number of the sequence, and the step argument is the difference between each number in the sequence.

a = range(5)
print(a) # range(0, 5)

a = range(1, 10, 2)
print(a) # range(1, 10, 2)

# Converting range to a list
a = list(range(5))
print(a) # [0, 1, 2, 3, 4]

a = list(range(1, 10, 2))
print(a) # [1, 3, 5, 7, 9]

# Iterative statements in python are: for, while, break, continue, pass

# The for loop is used to iterate over a sequence (list, tuple, string, etc.)
for i in range(5):
    print(i)

for i in range(13, 150, 13):
    print(i)

for i in range(1,21,2):
    print(i)

for i in range(50,0,-2):
    print(i)


# The while loop is used to execute a block of code as long as a condition is true
i = 0
while i < 5:
    print(i)
    i += 1

i= 10
while i > 0:
    print(i)
    i -= 1



# The break statement is used to exit the loop
for i in range(5):
    if i == 3:
        break
    print(i)

a =20
while a > 0:
    if a == 10:
        break
    print(a)
    a -= 1


# The continue statement is used to skip the current iteration and move to the next iteration
for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(1,15):
    if i ==5 or i == 7:
        continue
    print(i)

# The pass statement is used as a placeholder when a statement is required syntactically but no action is needed
for i in range(5):
    if i == 3:
        pass
    print(i)
>>>>>>> ff739ea4292d1023b6471ccecb899004abd38853

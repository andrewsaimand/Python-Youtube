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


# Python Quiz

# 1. Accpect two numbers and  print the greatest between them

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")

# 2. Accept the gender from the user as character (M/F) and print respective greeting message: Good Morning Sir/Good Morning Ma'am

gender = input("Enter your gender (M/F): ")

if gender == 'M' or gender == 'm':
    print("Good Morning Sir")
elif gender == 'F' or gender == 'f':
    print("Good Morning Ma'am")
else:
    print("Invalid input. Please enter 'M' or 'F'.")

# 3. Accept an integer and check whether it is even or odd


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

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# 4. Accept the age of a candidate and determine whether they are eligible for voting or not (age >= 18)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name} You are a valid voter")
elif age <18 and age >0:
    print(f"Hello {name} You arn't valid voter")
else:
    print("Give A valid age")


# 5. Accept a year and check if a leap year or not

year = int(input("Please Tell Your Year:"))

if year %4 ==0 and year %100 !=0:
    print("Its Leap Year")
elif year %100 ==0 and year %400 ==0:
    print("Its century leap year")
else:
    print("Its Not leap year")


# 6. Accept an english alphabet from user and check if it is a consonant or a vowel

word = input("Please tell your word:")

if word in "a,e,i,o,u" or word in "A,E,I,O,U":
    print(f"This {word} is vowel")
else:
    print(f"This {word} is consonant")


# 7. Print natural number up to n

n = int(input("Please Tell Your Number:"))

for i in range(1,n+1):
    print(i)

# 8. Reverse For loop print n to 1

n = int(input("Please Enter Your Number"))

for i in range(n,0,-1):
    print(i)


# 9. Take a Number as input and print a table

number = int(input("Please Tell Your Number:"))

for i in range(number,(number*10)+1,number):
    print(i)

number = int(input("Please Tell Your Number:"))

for i in range(1,11) :
    print(f"{number} * {i} = {number*i}")


# 10. Sum up to n term

number = int(input("Please Tell Your Number:"))

sum = 0

for i in range(1,number+1):
    sum = sum + i

print(sum)


# 11. factorial of a number

number = int(input("Please Tell Your Number:"))

sum = 1
for i in range(1, number+1):
    sum =sum * i

print(sum)


# 12. Print all the factors of a number

number = int(input("Please Tell Your Number:"))

for i in range(1, number+1):
    if number%i == 0:
        print(i)


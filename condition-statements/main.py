# condition statements
# if, elif, else, nested if, nested if-else, nested if-elif-else

# if statement?
# if statement is used to check
# the condition and execute the code if the condition is true

# if statement syntax
# if condition:
#     code to execute

# x = 100
#
# if x>20:
#     print("x is greater than 20")
# else:
#     print("x is less than 20")

# a=20
# b=40

# x = 100
# y = 20
# z = 30
#
# if x > y and x > z:
#     print("x is greater than y and z")
# elif y > x and y > z:
#     print("y is greater than x and z")
# else:
#     print("z is greater than x and y")

# age
# 18< and age>40

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are not eligible to vote")
# elif age >= 18 and age <=40:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# WAP to enter any number and check if it is even or odd
# num = int(input("Enter any number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# WAP to enter any number and check if is divisible by 3 and 5

# num = int(input("Enter any number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("Divisible by 3 and 5")
# else:
#     print("Not divisible by 3 and 5")

# nepali, english, maths, science, social
# total
# percentage
# grade: 35> 45<: C, 45> 55<: B, 55> 65<: A, 65> 75<: A+, 75> 85<: A++


# admin admin002
# ram ram002

# username = input("Enter username: ")
# password = input("Enter password: ")
#
# if username == 'admin' and password == 'admin002' or username == 'ram' and password == 'ram002':
#     print(f"welcome {username}")
#
# else:
#     print("Invalid username or password")

# users=[
#     {'username':'admin','password':'admin002'},
#     {'username':'ram','password':'ram002'},
# ]

#
# x = 100
# y = 20
# z = 10
#
# if x > y and x > z:
#     print("x is greater than y and z")
# elif y > x and y > z:
#     print("y is greater than x and z")
# else:
#     print("z is greater than x and y")


# nested if

# x = 25
# y = 20
# z = 30
#
# if x > y:
#     if x > z:
#         print("x is greater than y and z")
#     else:
#         print("z is greater than x and y")
#
# else:
#     if y > z:
#         print("y is greater than x and z")
#     else:
#         print("z is greater than x and y")

# username = input("Enter username:")
# password = input("Enter password:")
#
# if username == 'admin':
#     if password == 'admin002':
#         print("Welcome admin")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username")

#
# print("1. addition 2. subtraction 3. multiplication 4. division")
# option = int(input("Enter option: "))
#
# if option == 1:
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
#     print(f"Addition of {x} and {y} is {x + y}")
# elif option == 2:
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
#     print(f"Subtraction of {x} and {y} is {x - y}")
# elif option == 3:
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
#     print(f"Multiplication of {x} and {y} is {x * y}")
# elif option == 4:
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
#     print(f"Division of {x} and {y} is {x / y}")
# else:
#     print("Invalid option")

# x,y,z
# 7,6,8
# 8,7,6

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x > y:
    if x > z:
        if y > z:
            print(x, y, z)
        else:
            print(x, z, y)
    else:
        print(z, x, y)
else:
    if y > z:
        print(y, z, x)
    else:
        print(z, y, x)

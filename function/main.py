# what is function?
# function is a block of code which only runs when it is called.

# rules for creating function
# 1. function block start with def keyword
# 2. function name should be in camel case
# 3. function name should be in small case

# def hello():
#     print("hello world")
#
#
# hello()


# function with parameter

# def hello(name):
#     print("hello " + name)
#
# hello("sachin")

# function with return value
#
# def hello():
#    return ['ram','shyam','hari']
#
# print(hello())

# optional parameter

# def user(name,age=''):
#     print("name is "+name)
#     print("age is "+str(age))
#
# user("sachin")


# function scope
# global variable: variable which is defined outside of function
# local variable: variable which is defined inside of function


# def test():
#     x = 10
#
#
# test()
#
# print(x)

# x = 10
#
#
# def test():
#     global x
#     x = x + 40
#     print(x)
#
#
# test()
# print(x)


# def users(*names):
#     print(names)
#
#
# users("ram",'sita','hari')

# def total(*numbers):
#     total = 0
#     for number in numbers:
#         total = total + number
#
#     return total
#
#
# print(total(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))


# def users(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# users('ram', 'sita', 'hari', name='sachin', age=20, city='kathmandu')

# what is lambda function?
# lambda function is a small anonymous function
# lambda function can take any number of
# arguments but can only have one expression

# def add(a,b):
#     return a+b

# add = lambda a,b: a+b
# print(add(10,20))


# what is recursion?
# recursion is a process of calling function itself


# factorial of 5 = 5*4*3*2*1 = 120

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))
#
# def my_rep(data,times):
#     x=1
#     while x<=times:
#         print(data)
#         x+=1
#
#
# print(my_rep('hello',3))


# what is pass?
# pass is a keyword in python
# pass is used to avoid error
# pass is used to avoid error when we are not sure what to write in function


# def user():
#     pass
#
# print(user())

# def a():
#     return 100
#
# def b():
#     print(a())
#
# b()

# def add(a, b):
#     return a + b
#
#
# def total(any_function, a, b):
#     print(any_function(a, b))
#
#
# total(add, 10, 20)

#
# def take_value():
#     p = int(input("Enter the principal amount: "))
#     r = int(input("Enter the rate of interest: "))
#     t = int(input("Enter the time period: "))
#     return [p, r, t]
#
#
# def calculator():
#     x, y, z = take_value()
#     return x * y * z / 100
#
#
# def display():
#     print("The simple interest is: ", calculator())
#
# display()


# def get_marks():
#     nepali = float(input("Enter the marks of Nepali: "))
#     english = float(input("Enter the marks of English: "))
#     science = float(input("Enter the marks of Science: "))
#     social = float(input("Enter the marks of Social: "))
#     math = float(input("Enter the marks of Math: "))
#     return [nepali, english, science, social, math]
#
# def total():
#     x, y, z, a, b = get_marks()
#     return x + y + z + a + b
#
#
# def percentage():
#     return total() / 5

#
# def division():
#     if percentage() >= 80:
#         print("First Division")
#     elif percentage() >= 60:
#         print("Second Division")
#     elif percentage() >= 40:
#         print("Third Division")
#     else:
#         print("Fail")


# nested function
# module

# message = "ram ram sita gita gita gita hari hari hari hari gopal"
#
#
# def check_repeat(text):
#     data = {}
#     for word in text.split():
#         if word in data:
#             data[word] += 1
#         else:
#             data[word] = 1
#     return data
#
#
# res = check_repeat(message)
#
# largest = 0
# largest_key = ''
# data = []
#
# for key, value in res.items():
#     if value > largest:
#         largest = value
#         largest_key = key
#     data.append(value)
#
# equal=[]
# for x in data:
#     if data.count(x) > 1:
#         equal.append(x)
#
# print(res)
# print("largest",largest_key, largest)
# for x in res.items():
#     if x[1] in equal:
#         print("equal",x[0],x[1])


# course = "python programming"
# get not repeated character

# data = []
# for x in course:
#     data.append(x)
#
#
# for y in data:
#     if data.count(y) == 1:
#         print(y)


# for x in course:
#     if x in data:
#         data[x]+=1
#     else:
#         data[x]=1
#
# print(data)

# 1,2,3


# print(res.values())
# print(res.keys())
# print(dir(res))
# print(type(res))

# users=[1,2,3,4,5]
#
# for a in users:
#     print(a)
#
# for y range(10):
#     print(y


# class Test:
#     pass
#
# obj = Test()


# def users():
#     print("hello")
#
# users()

# data = [
#     [1, 2, 3, 5],
#     [4, 5, 6, 7],
#     [7, 8, 9, 10]
# ]
#
# total = 0
# for num in data:
#     for n in num:
#         total += n
#
# print(total)

# data = {'name': 'ram', 'address': 'kathmandu', 'age': 20}
# print(f"\n Name: {data['name']} \n Address: {data['address']} \n Age: {data['age']}")

users = [
    {'name': 'ram', 'address': 'kathmandu', 'age': 20,'gender':'male'},
    {'name': 'hari', 'address': 'bhaktapur', 'age': 30,'gender':'male'},
    {'name': 'sita', 'address': 'lalitpur', 'age': 40,'gender':'female'},
]

# print(users[0].values())

# for user in users:
#     print(f" Name: {user['name']}  Address: {user['address']}  Age: {user['age']}")
    # break

#
# print(data[1])

# numbers =[1,2,3,4,5,6,7,8,9,10]
# total =0
# for x in numbers:
#     total+=x
#
# print(total)

# What is loop?
# Loop is a way to repeat a block of code multiple times.
# There are two types of loops in python:
# 1. for loop
# 2. while loop
# 3. Nested loop

# for loop?
# for loop is used to iterate over a
# sequence (list, tuple, string) or other iterable objects.

# Syntax:
# for val in sequence:
#     body of for


# data = ['ram', 'shyam', 'hari', 'gita']
#
# for name in data:
#     print(name)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# total_even = 0
# total_odd = 0
# for num in numbers:
#     if num % 2 == 0:
#         total_even += 1
#     else:
#         total_odd += 1
#
# print(f"Total even numbers: {total_even}")
# print(f"Total odd numbers: {total_odd}")
#
# data = ['ram', 'shyam', 'hari', 'gita', 'ram', 'ram', 'gita']
# total_ram = 0
# total_gita = 0
# for name in data:
#     if name == 'ram':
#         total_ram += 1
#     elif name == 'gita':
#         total_gita += 1
#
# print(f"Total ram: {total_ram}")
# print(f"Total gita: {total_gita}")

# data = [
#     ['ram', 'shyam', 'hari', 'gita'],
#     ['sophia', 'sara', 'susan', 'sophie'],
#     ['john', 'james', 'jim', 'joe']
# ]
#
# for user in data:
#    for name in user:
#             print(name)

# num =int(input("Enter a number: "))
# names=[]
# for i in range(num):
#     name =input("Enter a name: ")
#     names.append(name)
#
# for n in names:
#     print(n)


# while loop?
# while loop is used to iterate over
# a block of code as long as the test expression (condition) is true.

# Syntax:
# while test_expression:
#     Body of while


# x = 1
# total_even = 0
# total_odd = 0
# while x <= 10:
#     if x % 2 == 0:
#         total_even += 1
#     else:
#         total_odd += 1
#     x += 1
#
# print(f"Total even numbers: {total_even}")
# print(f"Total odd numbers: {total_odd}")

# users = ['ram', 'sita', 'ram', 'ram']
#
# x = 0
#
# while x < len(users):
#     if users[x] == 'ram':
#         print(users[x])
#     x += 1

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a=0
# while a<len(number):
#     if number[a]%2==0:
#         print(number[a])
#     a+=1

# for user in users:
#     if user == 'ram':
#         print(user)

# num_time = int(input("Enter a number of times: "))
# increment = 1
# rep_number = []
# list_of_number = []
#
# while increment <= num_time:
#     number = int(input("Enter a number: "))
#     if not number in rep_number:
#         rep_number.append(number)
#     else:
#         list_of_number.append(number)
#
#     increment += 1
#
# # print(rep_number)
# print(list_of_number)

# 1x1=1
# 1x2=2


# num_of_students = int(input("Enter a number of students: "))
# increment = 1
# total_marks = []
#
# while increment <= num_of_students:
#     print(f"=============Student Id: {increment}=============")
#     for i in range(1):
#         nepali = int(input("Enter a marks of nepali: "))
#         english = int(input("Enter a marks of english: "))
#         science = int(input("Enter a marks of science: "))
#         social = int(input("Enter a marks of social: "))
#         math = int(input("Enter a marks of math: "))
#         total = nepali + english + science + social + math
#         total_marks.append(total)
#     increment += 1
#
# sId = 1
# for mark in total_marks:
#     total = mark
#     percentage = mark / 5
#     grade = ''
#     if percentage >= 80:
#         grade = 'A'
#     elif percentage >= 70:
#         grade = 'B'
#     elif percentage >= 60:
#         grade = 'C'
#     elif percentage >= 50:
#         grade = 'D'
#     elif percentage >= 40:
#         grade = 'E'
#     else:
#         grade = 'F'
#
#     print('=======================')
#     print(f"Student Id: {sId}")
#     print(f"Total marks: {total}")
#     print(f"Percentage: {percentage}")
#     print(f"Grade: {grade}")
#     sId += 1
#     print('=======================')

# data = [
#     {'name': 'ram', 'gender': 'male'},
#     {'name': 'sophia', 'gender': 'female'},
#     {'name': 'rita', 'gender': 'female'},
# ]

# data = []
# num_of_time = int(input("Enter a number of time: "))
# x = 1
# while x <= num_of_time:
#     name = input("Enter a name: ")
#     gender = input("Enter gender: ")
#     new_data = {"name": name, "gender": gender}
#     data.append(new_data)
#     x += 1
# total_male = 0
# total_female = 0
# for user in data:
#     if user['gender'] == 'male':
#         total_male += 1
#     else:
#         total_female += 1
# print(total_male)
# print(total_female)

# data = [
#     {
#         'name': 'ram',
#         'address': {'city': 'kathmandu'}
#     },
#     {
#         'name': 'sita', 'address': {'city': 'bhaktapur'}
#     },
#     {
#         'name': 'hari', 'address': {'city': 'lalitpur'}
#     },
# ]
#
# for user in data:
#     print(f"Name: {user['name']} City: {user['address']['city']}")


# data = [
#     {'name': 'ram', 'gender': 'male', 'status': True},
#     {'name': 'sophia', 'gender': 'female', 'status': False},
#     {'name': 'rita', 'gender': 'female', 'status': True},
#     {'name': 'laxmi', 'gender': 'female', 'status': True},
#     {'name': 'kabita', 'gender': 'female', 'status': True},
#     {'name': 'gopal', 'gender': 'male', 'status': False},
# ]
#
# total_active_users = 0
# total_inactive_users = 0
# total_active_male = 0
# total_inactive_male = 0
# total_active_female = 0
# total_inactive_female = 0
#
# total_users = len(data)
# for user in data:
#     if user['status'] == True:
#         if user['gender'] == 'male':
#             total_active_male += 1
#         if user['gender'] == 'female':
#             total_active_female += 1
#         total_active_users += 1
#     else:
#         if user['gender'] == 'male':
#             total_inactive_male += 1
#         if user['gender'] == 'female':
#             total_inactive_female += 1
#         total_inactive_users += 1
#
# print(f"Total User {total_users}")
# print(f"Total active users: {total_active_users}")
# print(f"Total inactive users: {total_inactive_users}")
# print(f"Total active male: {total_active_male}")
# print(f"Total active female {total_active_female}")
# print(f"Total inactive male: {total_inactive_male}")
# print(f"Total inactive female {total_inactive_female}")

# number = [1, 29, 3, 4, 5, 6, 78, 88, 9, 10]

# what is oop?
# oop is a programming paradigm based on the concept of "objects",
# which can contain data, in the form of fields (often known as
# attributes or properties),
# and code, in the form of procedures (often known as methods).

# what is object?
# An object is an instance of a class.
# A class is a template or blueprint from which objects are created.
# So, an object is the instance(result) of a class.

# data=['ram']
# data.append('shyam')

# class Students:
#     name ='ram'
#     age = 34
#
#     def student_info(self):
#         print('Name: ',self.name)
#         print('Age: ',self.age)
#
#     def add(self,x,y):
#         return x+y
#
# obj = Students()
# obj.student_info()
# print(obj.add(4,5))
#
# class Calculator:
#     def add(self, x, y):
#         return x + y
#
#     def sub(self, x, y):
#         return x - y
#
#
# obj = Calculator()
# print(obj.add(4, 5))
# print(obj.sub(4, 5))

# class SPI:
#     def take_value(self,p,t,r):
#         return p*t*r/100
#
# obj = SPI()
# print(obj.take_value(1000,2,3))

# class Students:
#     data = [
#         {'name': 'ram', 'age': 34, 'address': 'ktm'},
#         {'name': 'shyam', 'age': 34, 'address': 'ktm'},
#         {'name': 'hari', 'age': 34, 'address': 'ktm'},
#     ]
#
#     def show(self):
#         for user in self.data:
#             print('Name: ', user['name'])
#             print('Age: ', user['age'])
#             print('Address: ', user['address'])
#             print('----------------------')
#
#
# obj = Students()
# obj.show()


# class SPI:
#     def take_value(self):
#         p = int(input('Enter p: '))
#         t = int(input('Enter t: '))
#         r = int(input('Enter r: '))
#         return [p, t, r]
#
#     def calculator(self):
#         p, t, r = self.take_value()
#         return p * t * r / 100
#
#     def display(self):
#         print('The simple interest is: ', self.calculator())
#
#
# obj = SPI()
# obj.display()


# class College:
#     students = []
#
#     def add_students(self):
#         name = input('Enter name: ')
#         email = input('Enter email: ')
#         address = input('Enter address: ')
#         self.students.append({'name': name, 'email': email, 'address': address})
#
#     def show_students(self):
#         for student in self.students:
#             print('Name: ', student['name'])
#             print('Email: ', student['email'])
#             print('Address: ', student['address'])
#             print('------------------------')
#
# obj=College()
# obj.add_students()
# obj.show_students()

# class Students:
#     def __init__(self, name, age):
#         self.full_name = name
#         self.age = age
#
#     def user_info(self):
#         print('Name: ', self.full_name)
#         print('Age: ', self.age)
#
#
# obj = Students('ram', 23)
# obj.user_info()

# class Calculator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def add(self):
#         return self.x + self.y
#
#     def sub(self):
#         return self.x - self.y
#
#     def mul(self):
#         return self.x * self.y
#
#
# obj = Calculator(4, 5)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())


# class Students:
# def __str__(self):
#     return 'I am string method'

# def __init__(self):
#     print("I am constructor")
#
# def __del__(self):
#     print("I am destructor")


# obj = Students()
# print(obj)


class Students:
    data = [
        {'name': 'ram', 'address': 'ktm'},
        {'name': 'shyam', 'address': 'ktm'},
        {'name': 'hari', 'address': 'ktm'},
        {'name': 'gita', 'address': 'ltp'},
        {'name': 'gita', 'address': 'bkt'},
    ]

    def kathmandu(self):
        for info in self.data:
            if info['address'] == 'ktm':
                print(info)

    def ltp(self):
        for info in self.data:
            if info['address'] == 'ltp':
                print(info)

    def bkt(self):
        for info in self.data:
            if info['address'] == 'bkt':
                print(info)
    def add_user(self):
        pass

obj = Students()
obj.kathmandu()
# obj.ltp()
# obj.bkt()

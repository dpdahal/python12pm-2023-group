# what is data type?
# data type is a type of data
# data type is a type of variable

# two types of data type
# 1. primitive data type: int, float, complex, str, bool
# 2. non primitive data type: list, tuple, dict, set

# what is primitive data type?
# primitive data type is a data type which is not a collection of data

# what is non primitive data type?
# non primitive data type is a data type which is a collection of data

# what is int?
# int is a data type which is used to store integer(number) value
# positive number, negative number, zero
# example: 10, 20, 30, 40, 50
# a = 2345678987654

# what is float?
# float is a data type which is used to store decimal value
# example: 10.5, 20.5, 30.5, 40.5, 50.5
# num = 0345.76556787
# num = 345.76556787
# print(f"{num:.2f}")

# what is complex?
# complex is a data type which is used to store complex number
# example: 5+6j, 5+7j, 5+8j, 5+9j, 5+10
# real part: 5
# imaginary part: 6, 7, 8, 9, 10

# x = input("Enter x: ")
# print(type(x))
# y = input("Enter y: ")
# print(x + y)


# type casting
# waht is type casting?
# type casting is a process of converting one data type to another data type
# int(), float(), str(), complex(), bool()

# x = '10'
# print(type(x))
#
# x = int(x)
# print(type(x))

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# print(x + y)

# what is list?
# list is a data type which is used to store multiple values
# list is a collection of data
# list is a mutable data type
# list is a ordered data type
# list is a indexed data type
# list is a iterable data type

# data = ['ram', 'sita', 'hari']
# print(data[-0])
# list index starts from 0

# data = [
#     ['ram', 'sita', 'gita'],
#     ['hari', 'shyam', 'mohan'],
#     ['suresh', 'ramesh', 'mahesh'],
#     ['sophia', [[[['python']]]], 'sara']
# ]
# print(data[3][1][0][0][0][0])

# print(data[2][0])

#
# data = ['ram', 'sita']
# print(dir(data))
# # print(data)
# data[0] = 'hari'
# print(data)


# 'append', 'clear', 'copy',
# 'count', 'extend', 'index',
# 'insert', 'pop', 'remove', 'reverse', 'sort'
# append: add a value at the end of the list
# data = ['hari']
# data.append(['ram','sita'])
# print(data)
# print(data)
# data.append('sita')
# print(data)


# data = ['ram', 'sita', 'sita']
# print(data.count('sita'))
# data.clear()
# print(data)

# extend: add multiple values at the end of the list
data = ['ram', 'sita']
data1 = ['hari', 'gita']
data.extend(data1)
print(data)

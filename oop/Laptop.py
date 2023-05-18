# what is inheritance:
# Inheritance is a way of creating a new class for using details of an existing class
# without modifying it.

# class Laptop:
#     def brand(self, b_name):
#         return "Brand Name is " + b_name
#
#
# class Dell(Laptop):
#     pass
#
#
# class HP(Laptop):
#     pass
#
# obj = Dell()
# print(obj.brand('Dell'))
#
# ob1 = HP()
# print(ob1.brand('HP'))


class Laptop:
    __x = 10

    def get(self):
        return self.__x
    def set(self, x):
        self.__x = x

obj = Laptop()
obj.set(20)
print(obj.get())
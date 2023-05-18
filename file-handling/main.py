# what is file?
# file is a named location on disk to store related information.

# file extension: .txt, .py, .jpg, .mp3, .mp4, .pdf, .exe

# open file

# open() function is used to open a file in python.

# mode: r, w, a, r+, w+, a+
# r: read mode
# w: write mode
# a: append mode
# r+: read and write mode
# w+: write and read mode
# a+: append and read mode


# obj = open("students.txt", 'w')
# obj.write("Hello World")
# obj.close()

# name,email,address,phone
#
# with open("students.txt", 'a') as obj:
#     name = input("Enter your name: ")
#     email = input("Enter your email: ")
#     address = input("Enter your address: ")
#     phone = input("Enter your phone: ")
#     obj.write(f"name:{name},email:{email},address:{address},phone:{phone}")
#     obj.write('\n')


with open("students.txt", 'r') as obj:
    # data = obj.read()
    # data = obj.readlines()
    data = obj.readline()
    print(data)
    # print(type(data))
    # for i in data:
    #     print(i)

def register():
    username =''
    password=''
    confirm_password=''

def login():
    username=''
    password =''


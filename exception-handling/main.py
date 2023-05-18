# what is exception handling?
# exception handling is a way to handle errors in a program
# it is a way to handle the error and continue run time the program
# without exiting the program

# list of exceptions
# 1. ZeroDivisionError
# 2. NameError
# 3. TypeError
# 4. ValueError
# 5. IndexError
# 6. KeyError
# 7. AttributeError
# 8. ImportError
# 9. RuntimeError
# 10. SyntaxError
# 11. IndentationError
# 12. TabError
# 13. SystemError
# 14. KeyboardInterrupt
# 15. EOFError
# 16. FloatingPointError
# 17. OverflowError

# try:
#     print(10 / 0)
# except Exception as e:
#     print("Error: ", e)
# finally:
#     print("This is the finally block")

# advantages of exception handling
# 1. it handles the error and continues the program
# 2. it makes the program more readable
# 3. it makes the program more maintainable
# 4. it makes the program more secure
# 5. it makes the program more robust
# 6. it makes the program more flexible
# 7. it makes the program more extensible
# 8. it makes the program more portable

# disadvantages of exception handling
# 1. it makes the program slow
# 2. it makes the program complex
# 3. it makes the program difficult to debug
# 4. it makes the program difficult to test
# 5. it makes the program difficult to maintain
# 6. it makes the program difficult to read


# bank amount transfer


# def transfer_amount(amount):
#     if amount > 10000:
#         raise Exception("Amount cannot be greater than 10000")
#     else:
#         print("Amount transferred successfully")
#
#
# try:
#     transfer_amount(8000)
# except Exception as e:
#     print("Error: ", e)
#
#
# def add(x,y):
#     pass
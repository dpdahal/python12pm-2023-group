# from calculator import add, sub
from calculator import *

print(add(1, 2))
print(sub(1, 2))


# import datetime
#
# b_date = datetime.date(2023, 5, 12)
# today = datetime.date.today()
#
# print(b_date - today)

# students = [
#     {'name': 'ram', 'birth_date': '2023-05-12'},
#     {'name': 'shyam', 'birth_date': '2023-03-12'},
#     {'name': 'hari', 'birth_date': '2023-04-24'},
# ]
#
# import datetime
#
# for student in students:
#     b_date = datetime.datetime.strptime(student['birth_date'], '%Y-%m-%d').date()
#     today = datetime.date.today()
#     if today > b_date:
#         day = today - b_date
#         print(f"{student['name']} {day.days} days passed his birthday")
#     elif today == b_date:
#         print(f"{student['name']}  has his birthday today")
#     else:
#         day = b_date-today
#         print(f"{student['name']} {day.days} has not passed his birthday")

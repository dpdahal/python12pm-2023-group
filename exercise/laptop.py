# print("===================Computer Bazar===================")
# print("1. Dell(Rs:20000) 2.Toshiba(Rs:30000) 3.MAC(Rs:50000)")
# option = int(input("Enter your option: "))
# product_name = ''
# dell_price = 0
# toshiba_price = 0
# mac_price = 0
# quantity = 0
# delivery_charge = 0
# plastic_bag = 0
# bag_price = 0
# git_box_price = 0
# tax_amount = 0
#
# if option == 1:
#     quantity = int(input("Enter quantity: "))
#     product_name = "Dell"
#     dell_price = quantity * 20000
#
# elif option == 2:
#     quantity = int(input("Enter quantity: "))
#     product_name = "Toshiba"
#     toshiba_price = quantity * 30000
#
# elif option == 3:
#     quantity = int(input("Enter quantity: "))
#     product_name = "MAC"
#     mac_price = quantity * 50000
# else:
#     print("Invalid option")
#     exit()
#
# print("Delivery Option: 1. Home Delivery(Rs:1000) 2. Pick Up(Rs:0)")
# delivery_option = int(input("Enter your option: "))
# if delivery_option == 1:
#     delivery_charge = 1000
#
# print("1. Plastic Bag: 500 2. Bag:(Rs 2000) 3. Gift Box(Rs 5000) 4. None")
# bag_option = int(input("Enter your option: "))
# if bag_option == 1:
#     plastic_bag = 500
#
# elif bag_option == 2:
#     bag_price = 2000
#
# elif bag_option == 3:
#     git_box_price = 5000
# else:
#     print("Invalid option")
#
# total = dell_price + toshiba_price + mac_price
# print("Location: 1. Kathmandu(Rs:13% tax) 2. Lalitpur 3. Bhaktapur")
# location = int(input("Enter your option: "))
# if location == 1:
#     tax_amount = total * 0.13
#
# grand_total = total + delivery_charge + plastic_bag + bag_price + git_box_price + tax_amount
# print("============Bill================")
# print("Product Name: ", product_name)
# print("Quantity: ", quantity)
# print("Delivery Charge: ", delivery_charge)
# print("Plastic Bag: ", plastic_bag)
# print("Bag: ", bag_price)
# print("Gift Box: ", git_box_price)
# print("Tax Amount: ", tax_amount)
# print("Grand Total: ", grand_total)

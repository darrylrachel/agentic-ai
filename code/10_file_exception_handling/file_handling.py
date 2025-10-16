# file = open("order.txt", "w")
# try:
#     file.write("Masala Chai - 2 cups")
# finally:
#     file.close()

with open("another_order.txt", "w") as file:
    file.write("ginger tea - 4 cups")
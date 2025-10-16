# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosa, it confirms the order.
# Otherwise, it says it's not available.
# Task:
#   * Tack snack input
#   * If it's "cookies" or "samosa", confirm the order
#   * Else, show unavailable

order = input("What snack would you like to order? ")

def snack_suggestion():
    if order == "Cookies" or order == "Samosa":
        print(f"Order confirmed: {order}.")
    else:
        print(f"Item {order} not available") 

snack_suggestion()


# One liner
# snack = input("What snack would you like to order? ")

# if snack == "Cookies" or snack == "Samosa":
#     print(f"Order confirmed: {snack}.")
# else:
#     print(f"Item {order} not available")
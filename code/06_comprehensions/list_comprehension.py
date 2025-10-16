# [expression for item in items if condition]

# List
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea",
]

iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

length_tea = [my_length for my_length in menu if len(my_length) > 12]
print(length_tea)
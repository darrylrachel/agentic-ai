# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# value = 13
# if (remainder := value % 5):
#     print(f"Not divisible, remainder is {remainder}")


# available_sizes = ["small", "medium", "large"]
# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")

number_list = [1, 20, 34, 56, 700, 23]

if (number_guessed := int(input("Enter a number guess: "))) in number_list:
    print(f"correct number")
else:
    print(f"{number_guessed} is the wrong number")
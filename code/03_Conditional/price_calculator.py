# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.
# Taks:
#   * Input: "small", "medium", "large"
#   * Small -> $10, Medium -> 15, Large -> $20
#   * If invalid: show "Unkown cup size"

user_choice = input("Chose a cup size: (s, m, l): ").lower()

def price_calculator():
    if user_choice == 's':
        print(f"The cost of your small tea is $10")
    elif user_choice == 'm':
        print(f"The cost of your medium tea is $15")
    elif user_choice == 'l':
        print(f"The cost of your large tea is $20")
    else:
        print(f"Unknown cup size")

price_calculator()
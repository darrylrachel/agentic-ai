# NUMBERS
#
#   Integers
#   Boolean
#   Real (floats, decimals)
#   Complex Numbers (ex. 2 + 3j) / (Will not touch on in course)

#######################################################################

# Integer

black_tea_grams = 14
ginger_grams = 3

total = black_tea_grams + ginger_grams
print(f"Total grams of base tea is: {total}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Remaining grams of base tea is: {remaining_tea}")

milk_liters = 7
servings = 4
milk_per_serving1 = milk_liters / servings
milk_per_serving2 = milk_liters // servings
print(f"Milk per serving is: {milk_per_serving1}")
print(f"Milk per serving is: {milk_per_serving2}")


total_tea_leaves_harvested = 1_000_000_000
print(f"Tea leaves harvested: {total_tea_leaves_harvested}")
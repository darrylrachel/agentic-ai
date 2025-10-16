# OBJECTS
# 
# What is an object?
#   Everything in python is an object
#
#   Object
#        identity
#        type
#        value (can be left empty)
#
#
#
#   Mutable & Immutable
#       Mutable can be chaged
#       Immutable cannot be changed

###############################################

sugar_amount = 2

print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12

print(f"Initial sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 2: {id(12)}")

# Initial sugar: 2
# ID of 2: 140717079725000

# Initial sugar: 12
# ID of 2: 140717079725320
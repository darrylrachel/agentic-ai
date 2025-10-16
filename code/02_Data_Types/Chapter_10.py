# DICTIONARY

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "Black Tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe["base"]}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

# Membership Testing
print(f"Is sugar is in the order? {'sugar' in chai_order}")

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order Details: (items): {chai_order.items()}")
# Mutable Data Types

ingredients = ["water", "milk", "black tea"]
print(f"Before: {ingredients}")

ingredients.append("sugar")
print(f"After: {ingredients}")

ingredients.remove("sugar")
print(f"After After: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")

holing_last_item = chai_ingredients.pop()
print(f"Last Item: {holing_last_item}")

raw_spice_data = bytearray(b"CINNAMON")
print(f"Bytes: {raw_spice_data}")

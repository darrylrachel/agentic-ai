# SETS is just like joins in SQL

essential_spices = {
    "cardamom",
    "ginger",
    "cinnamon"
}

optional_spices = {
    "cloves",
    "ginger",
    "black pepper"
}

#  Union ( | )
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# Intersection ( & )
common_spices = essential_spices & optional_spices
print(f"Common Spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices ? {'cloves' in optional_spices}")

# Frozen Set

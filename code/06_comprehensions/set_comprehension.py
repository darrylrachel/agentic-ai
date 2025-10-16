# {expression for item in items if condition}

# Set
favorite_chai = [
    "Green Tea",
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea",
    "Iced Peach Tea",
]


unique_chai = { chai for chai in favorite_chai }
unique_chai = { chai for chai in favorite_chai if len(chai) > 8 }
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardmom", "clove"],
    "Elaichi Chai": ["cardmom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = { spice for ingredients in recipes.values() for spice in ingredients }
print(unique_spices)        
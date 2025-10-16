# You're creating a tea menu board.
# Each item ust be numbered.
# Task:
#     * Use enumerate() to print the menu items with numbers.

menu = ["Green Tea", "Chamamile Tea", "Water", "Lemon Ginger Tea", "Peach Tea"]

for idx, menu_item in enumerate(menu, start=1):
    print(f"Menu Item {idx} : {menu_item}")
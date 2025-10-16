# You're preparing an order summary with customer names and their total bill
# Task:
#     * Use two lists: one for names and one for bills
#     * Print: "[Name] paid $[amount]"

names = ["Darryl", "Ciera", "Sabriya", "Miakoda"]
bills = [24, 32, 5, 3]

for name, amount in zip(names, bills):
    print(f"{name} paid ${amount}")
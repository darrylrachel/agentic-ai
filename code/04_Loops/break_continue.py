# Some chai flavors are out of stock.
# You want to skip those and stop entirely if someone requests a restriced flavor 
# Task:
#     * Skip if flavor is "Out of Stock"
#     * Break if flavor is "Discontinued"

flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavor in flavors:
    if flavor == "Out of Stock":
        continue
    if flavor == "Discontinued":
        break
    print(f"Discontinued item found")

print(f"Outside of loop")
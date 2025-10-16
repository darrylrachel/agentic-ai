# You sell different chai sizes.
# Instead of writing formulas everywhere, create a function.
# Task:
#   * Write calculate_bill(cups, price_per_cup)
#   * Return total bill
#   * Use this for multiple orders

def calculate_bill(cups, price_per_cup):
    order_total = cups * price_per_cup
    #print(f"Your total is ${order_total} dollars")
    return f"Your total is ${order_total} dollars"

print(calculate_bill(2, 5))
calculate_bill(4, 2)
calculate_bill(2, 6)
calculate_bill(1, 8)
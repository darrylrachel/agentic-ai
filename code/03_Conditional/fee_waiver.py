# You are running an onlone tea store.
# If the order amount is more than $20 devlivery is free;
# otherwise, it cost $5 for delivery.
# Task:
#   * Input: "order_amount"
#   * Use ternary operator to decide delivery fee

order_amount = int(input("Enter the order amount: "))

delivery_fee = 0 if order_amount > 20 else 5

print(f"Your delivery fee is {delivery_fee} dollars")
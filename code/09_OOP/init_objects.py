class Chai_order:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = Chai_order("Masala", 200)
print(order.summary())

order_two = Chai_order("Ginger", 220)
print(order_two.summary())
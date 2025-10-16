class Chaicup:
    size = "small"

    def describe(self):
        return f"A {self.size} cup of chai"
    
cup = Chaicup()
print(cup.describe())
#print(Chaicup.describe()) # Missing required argument
print(Chaicup.describe(cup))


        
class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
print("After changing ", cutting.temperature)
print("Direct look into the class ", Chai.temperature)
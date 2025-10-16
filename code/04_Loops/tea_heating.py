# You want to simulate tea heating.
# It starts at 40C and boils at 100C.
# Task:
#     * Use a whioe loop.
#     * Increase temperature by 15 until it reaches 100. 
#     * Print each temperature step.

temperature = 40

while temperature < 100:
    temperature += 15
    print(f"Water temp is: {temperature}")

print(f"Water is boiling.")
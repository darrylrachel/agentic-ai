def pure_chai(cups):
    return cups * 10

total_chai = 0

# Not Recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups
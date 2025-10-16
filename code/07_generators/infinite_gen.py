def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai()

# _ variable placeholder
for _ in range(3):
    print(next(refill))
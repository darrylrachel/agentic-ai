import threading
import time

def prepare_chai(type_, wait_time):
    print(f"{type_} chai: Brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: Ready.")

# Creating the threads
t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 3))

start = time.time()

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Chai is ready in {end - start:.2f} seconds.")
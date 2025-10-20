# Daemon threads are background threads that automagically shuts down
# when the main program exits. Usually used for non-critical background
# tasks such as logging.

import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(3)

t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done")


# Non Daemon
def monitor_tea_temp2():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(3)

t2 = threading.Thread(target=monitor_tea_temp2)
t2.start()

print("Non Daemon, Main program done")
# You are building a smart thermostat alert system:
# If the device_status is "active"
#   And temperature > 35 -> Warn: "High temperature alert!"
#   Else: "Temperature normal"
# If device is off -> "Device is offline"

device_status = "active"
temperature = 90

def smart_thermostat():
    if temperature > 85 and device_status == "active":
        print(f"Warning: High temperature alert!")
    elif device_status == "off":
        print(f"Device is offline")
    else:
        print(f"Temperature normal")
    

smart_thermostat()
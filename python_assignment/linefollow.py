sensor = input ("enter 6 bit sensor data:")
if sensor =="001100":
    print("move forward")
elif sensor[:3].count('1')> sensor[3:].count('1'):
    print("turn left")
elif sensor[3:].count('1')> sensor[:3].count('1'):
    print("turn right")
elif sensor =="000000":
    print("stop")
else:
    print("adjust position ")
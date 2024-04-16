import serial
import json
import time
import random
from datetime import datetime

ser = serial.Serial(
    port= '/dev/ttyAMA10',
    baudrate=115200,
    timeout=1
)

def get_battery_data():
    timestamp = int(datetime.now().second)
    battery_voltage     = round(3.7  + (0.1 * random.random()), 2) #Spannung
    battery_current     = round(30   + (0.2 * random.random()), 2) #Stromstärke
    battery_capacity    = round(2600 - (100 * random.random()), 2) #Kapazität
    battery_soc         = round(100  - (10  * random.random()), 2) #State of Charge
    return {"timestamp":    timestamp, 
            "voltage":      battery_voltage, 
            "current":      battery_current, 
            "capacity":     battery_capacity, 
            "soc":          battery_soc}

try:
    while True:
        data = get_battery_data()
        json_data = json.dump(data).encode('utf-8') #Byte-Array

        ser.write(json_data)
        print("Sent: ", json_data)

        time.sleep(10)
except KeyboardInterrupt:
    ser.close()
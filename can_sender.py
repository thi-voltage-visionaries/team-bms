import os
import can
import time
import random
from datetime import datetime

#Create CAN-device
os.system('sudo ip link set can0 up type can bitrate 1000000 dbitrate 8000000 restart-ms 1000 berr-reporting on fd on')

#Configuration CAN0
can0 = can.interface.Bus(channel='can0', bustype='socketcan')

def get_battery_data():
    timestamp = int(datetime.now().second)
    battery_voltage     = round(3.7  + (0.1 * random.random())) #Voltage
    battery_current     = round(30   + (0.2 * random.random())) #Current
    battery_capacity    = round(2.6  - (0.1 * random.random())) #Capacity
    battery_soc         = round(10   - (10  * random.random())) #State of charge
    battery_temperature = round(40   + (5   * random.random())) #Temperature
    return {"timestamp":    timestamp, 
            "voltage":      battery_voltage, 
            "current":      battery_current, 
            "capacity":     battery_capacity, 
            "soc":          battery_soc,
            "temperature":  battery_temperature}

def send_data_on_can0(data):
    timestamp_int   =   int(data['timestamp'    ])
    voltage_int     =   int(data['voltage'      ])
    current_int     =   int(data['current'      ])
    capacity_int    =   int(data['capacity'     ])
    soc_int         =   int(data['soc'          ])
    temperature_int =   int(data['temperature'  ])

    #CAN-message
    msg = can.Message(is_extended_id=False, arbitration_id=0x123, 
                      data=[timestamp_int, voltage_int, current_int, capacity_int, soc_int, temperature_int])
    
    #Send over CAN0
    print(msg)
    can0.send(msg)

try:
    while True:
        battery_data = get_battery_data()
        send_data_on_can0(battery_data)
        time.sleep(10)
except KeyboardInterrupt:
    print("KeyboardInterrupt erhalten. Beende das Skript.")
finally:
    os.system('sudo ifconfig can0 down')
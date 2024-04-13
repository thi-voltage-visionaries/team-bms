import can
import os

os.system('sudo ip link set can1 up type can bitrate 1000000 dbitrate 8000000 restart-ms 1000 berr-reporting on fd on')

can1 = can.interface.Bus(channel='can1', bustype='socketcan')

try:
    while True:
        message = can1.recv()

        print('Received message:', message)
except KeyboardInterrupt:
    pass
finally:
    os.system('sudo ifconfig can1 down')


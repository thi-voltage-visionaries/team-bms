import can
import cantools

dbc = cantools.database.load.file('can_database.dbc')

bus = can.interface.Bus(channel='can0', bustype='socketcan')

for msg in bus:
    decoded_msg = dbc.decode_message(msg.arbitration_id, msg.data)
    print(decoded_msg)

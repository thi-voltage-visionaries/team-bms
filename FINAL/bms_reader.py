import json
import subprocess
import time
import os

# folder for all generated json files
output_folder = "battery_data_json"

while True:
    # open Daly-Smart-BMS UART message 
    output = subprocess.check_output(['daly-bms-cli', '-d', '/dev/ttyUSB0', '--all'])

    # transform message into json
    data = json.loads(output)

    # extract necessary data
    necessary_data = {
        "voltage": data["soc"]["total_voltage"],
        "current": data["soc"]["current"],
        "soc": data["soc"]["soc_percent"],
        "temperature": data["temperature_range"]["highest_temperature"],
        "capacity": data["mosfet_status"]["capacity_ah"]
    }

    # create filename with Unix timestamp
    timestamp = int(time.time())
    output_filename = f"battery_data_{timestamp}.json"
    output_file = os.path.join(output_folder, output_filename)

    # save json file in folder
    with open(output_file, 'w') as f:
        json.dump(necessary_data, f, indent=2)

    # wait 15 seconds
    time.sleep(15)

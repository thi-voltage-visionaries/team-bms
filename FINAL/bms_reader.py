import json
import subprocess
import time
import os

# Folder
output_folder = "battery_data"

while True:
    #Open Daly BMS UART message 
    output = subprocess.check_output(['daly-bms-cli', '-d', '/dev/ttyUSB0', '--all'])

    #Transform message into JSON
    data = json.loads(output)

    #Extract necessary data
    necessary_data = {
        "total_voltage": data["soc"]["total_voltage"],
        "current": data["soc"]["current"],
        "soc_percent": data["soc"]["soc_percent"],
        "temperature": data["temperature_range"]["highest_temperature"],
        "capacity_ah": data["mosfet_status"]["capacity_ah"]
    }

    #Create Filename with Unix timestamp
    timestamp = int(time.time())
    output_filename = f"battery_data_{timestamp}.json"
    output_file = os.path.join(output_folder, output_filename)

    #Save JSON in folder
    with open(output_file, 'w') as f:
        json.dump(necessary_data, f, indent=2)

    #Wait 20 seconds
    time.sleep(20)



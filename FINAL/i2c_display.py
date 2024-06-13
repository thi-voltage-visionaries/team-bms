import json
import os
import time
from datetime import datetime
from glob import glob
import drivers

# function to get latest json file from folder batter_data_json 
def get_latest_json_file(directory):
    files = glob(os.path.join(directory, "battery_data_*.json"))
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    return latest_file

# function to load the json file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# path of the folder
json_directory = '/home/test/Desktop/team-bms/battery_data_json'

# initialising drivers for lcd display
display = drivers.Lcd()

# background brightness of lcd display
display.lcd_backlight(1)

latest_file = None

try:
    while True:
        # find newest json file from folder
        new_file = get_latest_json_file(json_directory)
        # if there's a newer file, load and show new data
        if new_file and new_file != latest_file:
            print(f"Neue Datei gefunden: {new_file}")
            latest_file = new_file
            data = load_json(latest_file)
            # value extraction from json file
            voltage     = data.get('voltage', '')
            current     = data.get('current', '')
            soc         = data.get('soc', '')
            temp        = data.get('temperature', '')
            capacity    = data.get('capacity', '')
            # delete display
            display.lcd_clear()
            # current time
            clock = datetime.now()
            format_clock = clock.strftime("%H:%M:%S")
            # string build for each line on lcd display
            line1 = f"{format_clock}      {soc} %"
            line2 = f"V: {voltage} V  I: {current} A"
            line3 = f"C: {capacity} Ah"
            line4 = f"T: {temp} \337C"
            # show value on lcd display
            display.lcd_display_string(line1, 1)
            display.lcd_display_string(line2, 2)
            display.lcd_display_string(line3, 3)
            display.lcd_display_string(line4, 4)
            # time sleep
            time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    display.lcd_clear()

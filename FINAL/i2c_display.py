import json
import os
import time
from glob import glob
import drivers

# Funktion um die neueste JSON-Datei zu finden
def get_latest_json_file(directory):
    files = glob(os.path.join(directory, "battery_data_*.json"))
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    return latest_file

# Funktion um JSON-Datei zu laden
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
json_directory = '/home/test/Desktop/team-bms/battery_data_json'

# Initialisierung LCD-Display
display = drivers.lcd()

latest_file = None

try:
    while True:
        # Finde die neueste JSON-Datei
        new_file = get_latest_json_file(json_directory)
        # Wenn es eine neue Datei gibt, lade und zeige die neuen Daten
        if new_file and new_file != latest_file:
            print(f"Neue Datei gefunden: {new_file}")
            latest_file = new_file
            data = load_json(latest_file)
            # Extraktion der Werte aus JSON-Datei
            voltage     = data.get('total_voltage', '')
            current     = data.get('current', '')
            soc         = data.get('soc_percent', '')
            temp        = data.get('temperature', '')
            capacity    = data.get('capacity_ah', '')
            # Display löschen
            display.lcd.clear()
            #Strings aufbauen
            line1 = str("V: ", voltage,"     I:", current)
            line2 = str("SOC: ", soc)
            line3 = str("Temp: ", temp)
            line4 = str("C: ", capacity)
            # Werte auf dem Display anzeigen
            display.lcd_display_string(line1, 1)
            display.lcd_display_string(line2, 2)
            display.lcd_display_string(line3, 3)
            display.lcd_display_string(line4, 4)
        
            time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()

import json
import os
import time
from glob import glob
from RPLCD.i2c import CharLCD

# Funktion um die neueste JSON-Datei zu finden
def get_latest_json_file(directory):
    files = glob(os.path.join(directory, "*.json"))
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    return latest_file

# Funktion um JSON-Datei zu laden
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
json_directory = '/home/test/Desktop/team-bms/battery_data'

# Initialisierung LCD-Display
lcd = CharLCD(i2c_expander='PCF8574',
              address=0x27,
              port=1,
              cols=20,
              rows=4,
              charmap='A02',
              auto_linebreaks=True)

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
            lcd.clear()
            # Werte auf dem Display anzeigen
            # lcd.cursor_pos(0, 0) -> Position auf dem LCD-Display
            # lcd.write_string(voltage[:20]) -> Stellt sicher das es nicht über 20 Spalten geht
            # ... ergänzen ...
            time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()


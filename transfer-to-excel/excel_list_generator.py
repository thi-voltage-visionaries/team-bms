import openpyxl # mit pip3 install openpyxl in VSCode installieren
import random
import time
from datetime import datetime

# Funktion erstellt eine Excel Tabelle mit den Spaltenüberschriften Timestamp, Voltage, Current und Temperature
def create_excel_list(file_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Timestamp', 'Voltage', 'Current', 'Temperature'])
    wb.save(file_path)

# Funktion fügt die Batteriewerte vom BMS der Excel Tabelle hinzu
def append_to_list(file_path, data):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    ws.append(data)
    wb.save(file_path)

# Funktion holt sich die Batteriewerte vom BMS
def get_battery_data():
    #Platzhalter für das Auslesen des BMS
    #voltage = 3.6
    #current = 18
    #temperature = 38
    voltage = round(3.6 + (0.1 * random.random()), 2)
    current = round(5 + (10 * random.random()), 2)
    temperature = round (55 + (5 * random.random()))
    return [datetime.now(), voltage, current, temperature]

# Deklaration des Dateipfad
file_path = 'battery_data_list.xlsx' 

# Erstellt eine neue Excel Tabelle
create_excel_list(file_path)

# Liest die Batteriewerte vom BMS solange aus bis es durch eine Tastureingabe beendet wird z.B. control/Strg + C
try:
    while True:
        battery_data = get_battery_data()
        append_to_list(file_path, battery_data)
        print('Data is successfully transferred to Excel list')
        time.sleep(2) # Alle zwei Sekunden
except KeyboardInterrupt:
    print('Program is stopped by user')





# Team: BMS
Wie funktioniert das Python-Skript "battery_data.py"?

• Wenn das Programm ausgeführt wird, wird eine JSON-Datei erzeugt mit dem Titel "battery_data_{Unix-Zeitstempel}.json.

• Alle 10 Sekunden werden die Batteriewerte in einer neuen JSON-Datei abgespeichert.

• Abfrage läuft solange bis es durch den Nutzer beendet wird. (Strg/Control + C verwenden für Abbruch)

• Die erzeugten JSON-Dateien werden in einem seperaten Ordner mit dem Namen "battery_data" abgelegt.

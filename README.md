# Team: BMS
- Wie funktioniert das Python-Skript "battery_data.py"?

• Wenn das Programm ausgeführt wird, wird eine JSON-Datei erzeugt mit dem Titel "battery_data_{Unix-Zeitstempel}.json.

• Alle 10 Sekunden werden die Batteriewerte in einer neuen JSON-Datei abgespeichert.

• Abfrage läuft solange bis es durch den Nutzer beendet wird. (Strg/Control + C verwenden für Abbruch)

• Die erzeugten JSON-Dateien werden in einem seperaten Ordner mit dem Namen "battery_data" abgelegt.

- Setup 2-CH CAN FD HAT mit Raspberry Pi:

1. Step: Spannungspins des 2-CH CAN FD HAT auf 3.3 V einstellen

2. Step: SPI interface aktivieren: sudo raspi-config -> SPI -> Yes

3. Step: Neustart: sudo reboot

4. Step: python3 installieren

sudo apt-get update

sudo apt-get install python3-pip

sudo apt-get install python3-pil

sudo apt-get install python3-numpy

sudo pip3 install RPi.GPIO

sudo pip3 install spidev

sudo pip3 install python-can

5. Step: Dual SPI Mode aktivieren: 

sudo nano /boot/firmware/config.txt

6. Step: Hinzufügen folgender Commands am Ende der Datei: 

dtparam=spi=on

dtoverlay=spi1-3cs

dtoverlay=mcp251xfd,spi0-0,interrupt=25

dtoverlay=mcp251xfd,spi1-0,interrupt=24

7. Step: Baud rate einstellen:

sudo ip link set can0 up type can bitrate 1000000 dbitrate 8000000 restart-ms 1000 berr-reporting on fd on

sudo ip link set can1 up type can bitrate 1000000 dbitrate 8000000 restart-ms 1000 berr-reporting on fd on

8. Step: Buffer konfigurieren:

sudo ifconfig can0 txqueuelen 65536

sudo ifconfig can1 txqueuelen 65536

9. Step: CAN0 High mit CAN1 High und CAN0 Low mit CAN1 Low über Drahtbrücken verbinden

10. Step: Installation von can-utils:

sudo apt-get install can-utils

11. Step: Zwei Terminal Fenster öffnen

Fenster 1 "CAN-receiver": candump can0

Fenster 2: "CAN-sender": cansend can1 000#11.22.33.44

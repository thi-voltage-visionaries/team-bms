# Team: BMS

Both the UART-reader and I2C-display python file need to be started with two different ssh-connections via the terminal of your computer

How to start the UART-reader of the Daly Smart BMS:

1. Open the terminal
   
2. Write: cd Desktop/team-bms
   
   Included content:
   
   • folder for all generated json files
   
   • python file: bms_reader.py (UART-reader)
   
   • python file: automation_start.py (programm to automatically start all python files)

3. Start the UART-reader: python3 bms_reader.py
   

How to start the LCD-display for the Raspberry Pi 5:

1. Open the terminal
   
2. Write: cd lcd

   Included content:
   
   • Here you can find all the drivers for running the lcd panel via I2C
   
   • python file: i2c_display.py

4. Start the I2C-display: python3 i2c_display.py

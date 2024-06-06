# Team: BMS

Both the UART-reader and I2C-display python file need to be started with two different ssh-connections via the terminal of your computer

# How to start the UART-reader for the Daly Smart BMS

1. Open the terminal
   
2. Write: cd Desktop/team-bms
   
   Included content:
   
   • folder for all generated json files
   
   • python file: bms_reader.py (UART-reader)
   
   • python file: automation_start.py (programm to automatically start all python files)

3. Start the UART-reader: python3 bms_reader.py
   

# How to start the LCD-display for the Raspberry Pi 5

1. Open the terminal
   
2. Write: cd lcd

   Included content:
   
   • Here you can find all the drivers for running the lcd panel via I2C
   
   • python file: i2c_display.py

4. Start the I2C-display: python3 i2c_display.py

# Introduction to setup a new Raspberry Pi 5 to run these files

1. Setup the lithium cells to battery management system (BMS) and power supply
   
Wire the batteries to the BMS and the Power Supply like this:
   
![三元3串接线流程-英文_012](https://github.com/thi-voltage-visionaries/team-bms/assets/128964620/079fa2da-7106-407b-9c23-8b311a45efe0)

2. Connect the BMS to the Raspberry Pi:

Use the enclosed UART-USB cable to connect the BMS to Raspberry Pi.

Plug the 6-pin connector to BMS and USB-A port to the first USB-port of your Raspberry Pi.

3. Connect the I2C-display to Raspberry Pi like this:

<img width="647" alt="Bildschirmfoto 2024-06-06 um 15 03 04" src="https://github.com/thi-voltage-visionaries/team-bms/assets/128964620/a2301da1-ed09-4211-9fcc-c65d65edf7f0">

<img width="669" alt="Bildschirmfoto 2024-06-06 um 15 10 52" src="https://github.com/thi-voltage-visionaries/team-bms/assets/128964620/e80c005d-2181-47bb-b087-f35e08be1e55">

4. After the hardware setup you have to download some libraries

• Module for reading Daly-BMS data:

With "pip install dalybms" you download a python module the read out the BMS with bluetooth or UART.

Follow the steps on this website: https://pypi.org/project/dalybms/

• Repository for I2C-Display drivers:

Use "git clone https://github.com/the-raspberry-pi-guy/lcd.git" to download the repository to interface a 16x2 LCD display.

For more information check this website: https://github.com/the-raspberry-pi-guy/lcd

Save the i2c_display.py file also in this folder to be able to use the drivers.



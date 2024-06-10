# How to control batteries in combination with Daly Smart BMS and Raspberry Pi

<img src="https://github.com/thi-voltage-visionaries/team-bms/assets/128964620/4cfa2aeb-6bf4-47f2-9fbf-743a0f53c178" width="500" height="500">

In the folder **FINAL** you can find two python scripts **bms_reader.py** and **i2c_display.py**.

Both python files need to be started with two different ssh-connections via the terminal of your computer.

## How to start the UART-reader for the Daly-Smart-BMS
   
1. Open this folder:
   ```
   cd Desktop/team-bms
   ```
   **This folder contains:**
   
   - folder for all generated json files
   
   - python file: bms_reader.py

4. Start the python script:
   ```
   python3 bms_reader.py
   ```

## How to start the LCD-display for the Raspberry Pi
   
1. Open this folder:
   ```
   cd lcd
   ```
   **This folder contains:**
   
   - display drivers
   
   - python file: i2c_display.py

4. Start the python script:
   ```
   python3 i2c_display.py
   ```

# How to make your own battery reader from scratch

## Required components

- 2x Raspberry Pi 5 [Berrybase](https://www.berrybase.de/raspberry-pi-5-8gb-ram)

- 2x LORA-HATs for Raspberry Pi [Waveshare](https://www.waveshare.com/sx1262-868m-lora-hat.htm)

- I2C-Display for Raspberry Pi [AZ-delivery](https://www.az-delivery.de/products/hd44780-2004-lcd-display-bundle-4x20-zeichen-mit-i2c-schnittstelle)

- Logic Level Converter for I2C-Display [Amazon](https://www.amazon.de/RUNCCI-YUN-Pegelwandler-Converter-BiDirektional-Mikrocontroller/dp/B082F6BSB5/ref=sr_1_3?_encoding=UTF8&camp=1634&creative=19450&dib=eyJ2IjoiMSJ9.OLKnXLjUidtxb9dlbOWxIGBqWJDnqPNpjMAiVYI0MESMHnDKtkcQCbtqDpUZMEUHqONs70YYTJGiRWbgMoZ2CJ5pNFBcIFx6CBjXRs5GPeTxRZh71-w2KWPxHab5UsYhsV5jaJ3fmUw1dvEev4FKLE_FlJeDcYZS7rF5_1o_DMAkrW-R1GZftRxBkoJfxQIXLH_RpM416Uf2cHz2yivCbUsvurmLMbC14jwO1-S0CRI.c2B-xnxTEW7FHAqmawtGrlkS0XFL7QlWwRes5H5WPlE&dib_tag=se&keywords=3.3+5V+i2c+level&linkCode=ur2&qid=1717681807&sr=8-3)
 
- Daly Smart BMS 3S 12V 30A [Amazon](https://www.amazon.de/DALY-Programmierbares-Li-Ion-Batterieschutzplatine-CAN-Kommunikation-Batterieschutzmodul-Smart-BMS-UART-485-CAN-BT/dp/B0B52Z4C6F/ref=sr_1_1?__mk_de_DE=ÅMÅŽÕÑ&crid=2O0I0OU97RRUC&dib=eyJ2IjoiMSJ9.nfZpvxY-7ZKIyxBi8RKbjfCjSErGZKg5_FhlCucBPexAj9wTkxIEImSSBPyEfEyg7e2__jLER3yxW9w8YCyCREWONMV8udEGl8bccmqbqMAFCauyStXk3CNTbPODwtsv1Q_lBqTVNem7moq1reMF4iZ-TzhX-0utL_BP9JqPX512PalxOXu1uSvSechMJ0TY2yzxK8miVYdT0AK3pWQL5s-_ZGfSPG3e-3HwAwcwKt0.LQcR7npzQ7WvkFCZRL_Looyjln3xuhinC2Sh_9ZQJ8s&dib_tag=se&keywords=daly%2Bsmart%2Bbms%2B3s%2B12v%2B30a&qid=1717681620&sprefix=daly%2Bsmart%2Bbms%2B3s%2B12%2B%2Caps%2C422&sr=8-1&th=1)
       
- 3x 18650 Li-Ion battery cells [Akkushop](https://www.akkushop.de/de/sony-konion-us18650vtc5-2600mah-36v-37v-654x182mm-mit-loetfahne-u/?gad_source=1&gclid=CjwKCAjwvIWzBhAlEiwAHHWgvdeJbn3S9KlfwelRqTj_DZ0MY1e8mpTiXzy03aw5u1-dA221t2gdXxoCXokQAvD_BwE)

- Bracket for 18650 Li-Ion battery cells [Amazon](https://www.amazon.de/GTIWUNG-Batteriehalter-Kunststoff-Abdeckung-Aufbewahrungsbox-12-Stück-3-7V-18650/dp/B08PZ4GVSD/ref=sr_1_21_sspa?__mk_de_DE=ÅMÅŽÕÑ&crid=288J965ELF7C9&dib=eyJ2IjoiMSJ9.1452SChiDavnz1YhivqquYca_tJp86ORIDnJW353Ml1oX2DohscWspUeIrmTft39vLa3X1WFIn5fshwO4U748XGklUaM0RI3Yjh_1P1k9_wgwW3ZxwLB7ZA_l1fuT0B8qEBFyakF9ntQA7767P78tavIBfQ-AztMaKYF2MER2-fklkPSq8FC1Dx5OKZS_p4k-gFG48qUT4Te59V1s5rngGdis_ejAcsRoP_JcRmr_Tw.KzXsdC_9xJoPDr3ZES3HanyaVtXy3UmYDtpm09Brd2U&dib_tag=se&keywords=battery%2Bholder%2B18650%2Bsolder%2B3&qid=1717681553&sprefix=battery%2Bholder%2B18650%2Bsold%2B3%2Caps%2C427&sr=8-21-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9idGY&th=1)

- Breadboard [Amazon](https://www.amazon.de/Elegoo-Points-Mini-Breadboard-Arduino/dp/B01M9CHKO4/ref=sxin_12_pa_sp_search_thematic_sspa?__mk_de_DE=ÅMÅŽÕÑ&content-id=amzn1.sym.889d1a42-4b89-467a-a9a5-747ec57750bb%3Aamzn1.sym.889d1a42-4b89-467a-a9a5-747ec57750bb&cv_ct_cx=breadboard&dib=eyJ2IjoiMSJ9.YUpyuUfyhAe-QuOj86N8B4Xl0S1KZd-UUefZ3hghHWVHpvnZzneUXLTUs72tgnPUp7APk2KY_bWnnAdkpPdyXg.5uNhzuSYimW4fk3P033sIlraONMTj_rq4-krhF27TFE&dib_tag=se&keywords=breadboard&pd_rd_i=B01M9CHKO4&pd_rd_r=ece7bd6f-52b7-412a-b1aa-a44b00aa2dae&pd_rd_w=Iwc3W&pd_rd_wg=7sFuM&pf_rd_p=889d1a42-4b89-467a-a9a5-747ec57750bb&pf_rd_r=5NV5H2Q5Z7MSY7M6SZ04&qid=1717682207&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-2-0bff13d2-7188-4a82-bb3a-ccd1e70f0167-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1)

- Jumper Wire [Amazon](https://www.amazon.de/AZDelivery-Jumper-Arduino-Raspberry-Breadboard/dp/B074P726ZR/ref=sr_1_1_sspa?__mk_de_DE=ÅMÅŽÕÑ&crid=U696S9FIKARC&dib=eyJ2IjoiMSJ9.WJAp30y3xmTevyXePDnrp_oaTwr68QZamNQjrjcftBdB0zGBr6bgW-97MQJnxfJpR-s27F5iFIaKbe36rfV_So6OIqWfyJQpqUcMZGef_FXrbMAXtjfeeXLmnO_1GCNNS-DSEHiVIJ06ql_7hArXoDaVsjfkneaeEPnCRSOD-vxIyHLoeEUDN62E1kQAchujM0dccJ4YLzEbEY6uQx2dhviXCOrzAFnLu80h9pv7IqHKXFb3WmrOoksxSWPnyyNbNIl8XND1iW4ock2LTF2qgP9fWK3tULB5QWRBw9mQUPM.haaGgt8ou9lwMiIWONle99MYZAY8uM40JgO4ZOYBu3w&dib_tag=se&keywords=jumper+wire&qid=1717682280&s=computers&sprefix=jump%2Ccomputers%2C991&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)

## Step-by-Step Guide

### 1. Setup the Hardware
- Wire the three Li-Ion battery cells to the Daly-Smart-BMS:
   ![三元3串接线流程-英文_012](https://github.com/thi-voltage-visionaries/team-bms/assets/128964620/f7a5280a-7ee8-4864-bd47-6b999ed66ca1)


   **For more information check this website:** [Daly](https://www.dalybms.com/bms-wiring-tutorial-2/?_gl=1*t4qdqc*_up*MQ..*_ga*MTc5NzQzMzgxOS4xNzE4MDI3MjY5*_ga_QJJLNQB8EJ*MTcxODAyNzI2OC4xLjAuMTcxODAyNzI2OC4wLjAuMA..*_ga_RPN8G89S7P*MTcxODAyNzI2OC4xLjAuMTcxODAyNzI2OC4wLjAuMA..&gclid=CjwKCAjwyJqzBhBaEiwAWDRJVKBu5Kb6dW-XVRdvnflk8SaZ5ARGhr5n8a_GkJ4UVz-WR8ddkm-RZRoC_U0QAvD_BwE)

- Connect the Daly Smart BMS with the enclosed UART-USB-A cable to Raspberry Pi:

- Connect the I2C-display to Raspberry Pi with this Pinout:

<img width="600" alt="Bildschirmfoto 2024-06-06 um 15 03 04" src="https://github.com/thi-voltage-visionaries/team-bms/assets/128964620/a2301da1-ed09-4211-9fcc-c65d65edf7f0">

<img width="600" alt="Bildschirmfoto 2024-06-06 um 15 10 52" src="https://github.com/thi-voltage-visionaries/team-bms/assets/128964620/e80c005d-2181-47bb-b087-f35e08be1e55">

**For more information check this website:** [Tutorial-RaspberryPi](https://tutorials-raspberrypi.de/hd44780-lcd-display-per-i2c-mit-dem-raspberry-pi-ansteuern/)

### 2. Package installments

• Python Module for Daly-Smart-BMS:
```
pip install dalybms
```

**For more information check this website:** [PyPi](https://pypi.org/project/dalybms/)

• GitHub Repository for I2C-Display drivers:
```
git clone https://github.com/the-raspberry-pi-guy/lcd.git
```
**For more information check this website:** [GitHub](https://github.com/the-raspberry-pi-guy/lcd)

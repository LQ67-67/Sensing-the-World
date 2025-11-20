# Sensing-the-World
Raspberry Pi Projects with Explorer HAT Pro
## 🛠️ The Gear

Both projects utilize the **Explorer HAT Pro**, which mounts directly onto the Raspberry Pi's GPIO header111. This HAT provides a safe and easy way to connect sensors and LEDs using a mini-breadboard.

**Required Components:**

- Raspberry Pi 4 (or 3B+) with power supply2.
- Explorer HAT Pro3.
- 
    
    **Project 1:** TMP36 Analog Temperature Sensor4.
    
- 
    
    **Project 2:** 1x Blue LED, 1x Red LED, 2x 470Ω Resistors5555.
    
- 
    
    **Both:** 1x Buzzer and Jumper wires6.
    

If your Explorer HAT Pro isn't set up yet, you'll need to do the following:

```bash
curl https://get.pimoroni.com/i2c | bash
sudo apt-get install python-smbus
sudo apt-get install python-pip
sudo pip install explorerhat

```

Those commands will install set up I2C and install the Explorer HAT Python library.

Next, you'll want to plug your Explorer HAT Pro into the 40 pin GPIO connector on your Raspberry Pi. You can check it's working by typing the following straight in the terminal:

```bash
python -c 'import time, explorerhat; explorerhat.light.on(); time.sleep(1); explorerhat.light.off()'

```

That should light up all four of the LEDs on the Explorer HAT Pro board for a second and then switch them all off again. If that works, then your Explorer HAT Pro is good to go!

---

## Project 1: Sensing the World (Analog Input)

### 🌡️ The Smart Temperature Monitor

Our first goal is to build a dashboard that continuously monitors room temperature. If it gets too hot (over 30°C), a buzzer will sound an alarm7.

### Hardware Setup

The TMP36 sensor is sensitive, so wiring orientation is critical. Holding the sensor with the **flat face** toward you, the pins are 1, 2, and 3 from left to right8888.

**Wiring Map** (Refer to the image below):

- 
    
    **Vout (Pin 1/Left):** Connect to **Analog Input A1** (This sends the data)999.
    
- 
    
    **GND (Pin 2/Middle):** Connect to **GND**101010.
    
- 
    
    **+Vs (Pin 3/Right):** Connect to **5V**111111.
    
- 
    
    **Buzzer:** Connect Positive (+) to **OUT1** and Negative (-) to **GND**12.
    

**Visual Reference:**

https://cdn.learn.pimoroni.com/article/making-a-minecraft-thermometer/assets/thermometer-wiring.jpg?width=1024

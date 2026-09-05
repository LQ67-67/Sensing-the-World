
<!--
============================================
  🌍 Sensing the World
  Raspberry Pi · Explorer HAT Pro · Python
============================================


<p align="center">
  <img src="SensingTheWorld/logo.png" alt="Project Logo" width="200" height="200"/>
  <!-- REPLACE: put your logo in SensingTheWorld/logo.png -->
</p>


<h1 align="center">🌍 Sensing the World</h1>

<p align="center">
  <strong>Raspberry Pi Projects with Explorer HAT Pro</strong><br/>
  <em>Analog sensing, visual feedback, and smart alerts</em>
</p>

<p align="center">
  <!-- Badges – replace username/repo and actual values -->
  <a href="https://github.com/LQ67-67/Sensing-the-World">
    <img src="https://img.shields.io/badge/version-v1.0.0-blue" alt="Version"/>
  </a>
  <a href="https://github.com/LQ67-67/Sensing-the-World/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License"/>
  </a>
  <a href="https://github.com/LQ67-67/Sensing-the-World/actions">
    <img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build Status"/>
  </a>
  <a href="https://github.com/LQ67-67/Sensing-the-World/releases">
    <img src="https://img.shields.io/github/downloads/LQ67-67/Sensing-the-World/total" alt="Downloads"/>
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/platform-Raspberry%20Pi%20%7C%20Linux-lightgrey" alt="Platform"/>
  </a>
  <a href="https://github.com/LQ67-67/Sensing-the-World/issues">
    <img src="https://img.shields.io/github/issues/LQ67-67/Sensing-the-World" alt="Issues"/>
  </a>
  <a href="https://github.com/LQ67-67/Sensing-the-World/stargazers">
    <img src="https://img.shields.io/github/stars/LQ67-67/Sensing-the-World?style=social" alt="Stars"/>
  </a>
</p>

---

## 📖 Introduction

**Sensing the World** is a hands‑on Raspberry Pi project kit that teaches analog input, output control, and real‑time monitoring using the **Explorer HAT Pro** expansion board.  
It includes two self‑contained sub‑projects:

- 🌡️ **Smart Temperature Monitor** – reads an analog TMP36 sensor, displays data, and triggers a buzzer when temperature exceeds 30 °C.
- 💡 **LED Alert System** – blinks blue and red LEDs to indicate status (e.g., safe / warning).

Perfect for makers, educators, and IoT hobbyists who want to learn GPIO programming in Python.

---

## ✨ Features

- 🔌 **Plug‑and‑play hardware** – Explorer HAT Pro mounts directly on the GPIO header.
- 📊 **Analog‑to‑digital conversion** – read precise temperature values via the TMP36 sensor.
- 🚨 **Audible & visual feedback** – buzzer and LEDs provide immediate alerts.
- 🐍 **Pure Python** – simple, well‑commented code for beginners and experts.
- 🛠️ **Expandable** – easily add more sensors or actuators using the mini‑breadboard.

---

## 🖼️ Gallery

### System Overview

<p align="center">
  <img src="SensingTheWorld/architecture.png" alt="System Architecture" width="80%"/>
  <br/>
  <em>Figure 1 – High‑level block diagram of the project</em>
  <!-- REPLACE: add your architecture diagram -->
</p>

### Hardware Wiring

The TMP36 sensor wiring is critical – refer to the image below for correct pin connections.

<p align="center">
  <img src="SensingTheWorld/hardware-wiring.jpg" alt="Hardware Wiring Diagram" width="80%"/>
  <br/>
  <em>Figure 2 – TMP36 sensor and buzzer wiring on Explorer HAT Pro</em>
  <!-- REPLACE: you can use the official image: https://cdn.learn.pimoroni.com/article/making-a-minecraft-thermometer/assets/thermometer-wiring.jpg?width=1024, but download it to your repo -->
</p>

### Project Demos

<table align="center">
  <tr>
    <td align="center">
      <img src="SensingTheWorld/demo-temperature.png" alt="Temperature Monitor" width="300"/>
      <br/>
      <em>🌡️ Temperature reading in the terminal</em>
    </td>
    <td align="center">
      <img src="SensingTheWorld/demo-leds.gif" alt="LED Alert Animation" width="300"/>
      <br/>
      <em>💡 LED status indicator (blue = safe, red = alert)</em>
    </td>
  </tr>
  <!-- REPLACE: add your own screenshots / GIFs -->
</table>

---

## 🚀 Quick Start

### Prerequisites

- Raspberry Pi 4 / 3B+ (or any model with 40‑pin GPIO)
- Explorer HAT Pro board
- Micro‑SD card with Raspberry Pi OS (bullseye or later)
- Internet connection for initial setup

### Hardware Assembly

1. **Mount the Explorer HAT Pro** onto the GPIO header of your Raspberry Pi.
2. **Wire the components** as described in the gallery above (or refer to the `docs/` folder).

### Software Setup

Open a terminal on your Raspberry Pi and run the following commands to install the necessary I²C tools and the Explorer HAT Python library:

```bash
# Install I2C and Explorer HAT dependencies
curl https://get.pimoroni.com/i2c | bash
sudo apt-get install -y python-smbus python3-pip
sudo pip3 install explorerhat
```

> 💡 **Test your HAT**:  
> ```bash
> python3 -c 'import time, explorerhat; explorerhat.light.on(); time.sleep(1); explorerhat.light.off()'
> ```  
> All four LEDs on the HAT should flash briefly – if they do, you're ready!

### Run the Projects

Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/SensingTheWorld.git
cd SensingTheWorld
```

#### Project 1 – Temperature Monitor

```bash
python3 temperature_monitor.py
```

You'll see the current temperature printed every second. If it exceeds 30 °C, the buzzer will sound.

#### Project 2 – LED Alert

```bash
python3 led_alert.py
```

The LEDs will cycle blue/red to indicate different states (customize the logic in the script).

---

## 📁 Project Structure

```
SensingTheWorld/
├── SensingTheWorld/               # Image assets (your screenshots, diagrams)
│   ├── logo.png
│   ├── architecture.png
│   ├── hardware-wiring.jpg
│   ├── demo-temperature.png
│   └── demo-leds.gif
├── temperature_monitor.py         # Main script for Project 1
├── led_alert.py                   # Main script for Project 2
├── lib/                           # Helper modules (if any)
├── docs/                          # Additional documentation
├── tests/                         # Unit tests (optional)
├── requirements.txt               # Python dependencies
├── LICENSE
└── README.md                      # This file
```

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberry-pi&logoColor=white" alt="Raspberry Pi"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/I2C-007ACC?style=for-the-badge&logo=i2c&logoColor=white" alt="I2C"/>
  <img src="https://img.shields.io/badge/Explorer%20HAT-FF6F00?style=for-the-badge&logo=adafruit&logoColor=white" alt="Explorer HAT"/>
</p>

- **Hardware:** Raspberry Pi 4/3B+, Explorer HAT Pro, TMP36 sensor, LEDs, resistors, buzzer
- **Software:** Python 3, `explorerhat` library, I²C, Linux GPIO

---

## 🤝 Contributing

Contributions are welcome! Whether it’s a bug fix, new sensor support, or improved documentation – please feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/awesome-idea`
3. Commit your changes: `git commit -m 'Add awesome idea'`
4. Push to the branch: `git push origin feature/awesome-idea`
5. Open a Pull Request.

Please make sure your code is well‑commented and follows [PEP 8](https://peps.python.org/pep-0008/) style.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 🙏 Acknowledgements

- [Pimoroni](https://shop.pimoroni.com/) for the excellent Explorer HAT Pro and its library.
- The Raspberry Pi Foundation for the amazing single‑board computer.
- All contributors and makers who share their knowledge.

---

<p align="center">
  <strong>⭐ If this project helped you learn or build something cool, give it a star!</strong>
</p>

<!------------------------------------------ TITLE BLOCK --------------------------------------------------------------->
<h1 align="center"> MoodMesh </h1>

<p align="center">
    CSE 118 Team I
    <br /> <br />
    <a href="https://github.com/friidryce"> Jason Au </a>
    ·
    <a href="https://github.com/cstarrynight"> Christina Mai </a>
    ·
    <a href="https://github.com/kendrick010"> Kendrick Nguyen </a>
</p>


<!------------------------------------------ TABLE OF CONTENTS ---------------------------------------------------------->
<details open="open">
  <summary><h2 style="display: inline-block"> Table of Contents </h2></summary>
  <ol>
    <li>
      <a href="#about-the-project"> About The Project </a>
      <ul>
        <li><a href="#built-with"> Built With </a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started"> Getting Started </a>
      <ul>
        <li><a href="#prerequisites"> Prerequisites </a></li>
        <li><a href="#project-installation"> Project Installation </a></li>
        <li><a href="#how-to-run"> How to Run </a></li>
      </ul>
    </li>
    <li><a href="#network-architecture"> Network Architecture </a></li>
    <li><a href="#file-architecture"> File Architecture </a></li>
  </ol>
</details>


<!------------------------------------------ About The Project ---------------------------------------------------------->
## About The Project

A problem statement our project seeks to address is how environmental factors can impact mental health. We often spend time in places, such as home, work, school, etc., that have notable “environmental factors”, such as aesthetics, lighting, sound, people, etc. These ambient factors can psychologically affect our mental wellness; for instance, raising stress levels or induce symptoms from specific sensory sensitivities. Although this problem statement can apply to a general population, it mainly prioritizes people with mental health issues, such as depression and loneliness. 

To address the issue of the lack of awareness on how improvements in environmental factors could affect one’s mental health, our project is geared towards creating a wearable device and application that dynamically adjusts and monitors environmental factors, such as lighting, based on biometric data from heart rate stress levels, etc.

### Built With
- Galaxy Smart Watch
- Raspberry Pi
- Python
- Flask
- ESP32
- PlatformIO
- ngrok

<!------------------------------------------ Getting Started ---------------------------------------------------------->
## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

This project will be running on a Raspberry Pi. Set up your Raspberry Pi by installing the Raspberry Pi OS. If you are comfortable with using Linux, I recommend downloading the Raspberry Pi OS Lite version. Here is a [complete guide for installing the OS](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up).

Make sure you have the latest version of `Python 3.11.*` on your Raspberry Pi. 

For our wearable app, development and installation was done on [Android Studio](https://developer.android.com/studio) on a personal machine.

An optional portion of this project was designing and fabricating a smart light appliance. We prototyped a nano leaf, and the design files and BOM will be listed [here](smart_devices/README.md). The nano leaf is an IoT device, which requires embedded firmware for the ESP32 housed inside. Therefore, we recommend using [Visual Studio Code](https://code.visualstudio.com/) with the [PlatformIO](https://platformio.org/) extension for development.

Lastly, this project is persistently communicating with different devices, among the watch, server, and smart appliance. Our main method of communication is with REST APIs via HTTP requests. To make our device/server network endpoints public yet secure for communication, we require a tool [nrgok](https://ngrok.com/) on the Raspberry Pi. Feel free to use the free trial!

### Smart Appliance-Installation

1. Build the nano leaf as outlined [here](smart_devices/README.md).

2. Clone the repo on your personal machine
```bash
git clone https://github.com/friidryce/UCSD-CSE-118-218-Team-I
```

3. On [Visual Studio Code](https://code.visualstudio.com/), open a [PlatformIO](https://platformio.org/) project using the `esp32_nanoleaf/firmware` folder.

4. In the `esp32_nanoleaf/firmware/include` folder, create a `secrets.h` header file containing your WiFi credentials. This must be the same network that the Raspberry Pi is on. Example,
```c
// Wifi credentials
const char* ucsdSSID = "UCSD-Guest";
const char* ucsdPassword = "";
```

5. Upload the code `src` code to the ESP32. [PlatformIO](https://platformio.org/) offers convenient features, such as port detection, larger boards selection, pre-loaded libraries, and all other features offered already in VSCode, that makes embedded development easy.

6. Open the Serial Monitor and wait for a successful WiFi connection. Once connected, the Serial Monitor will print the local IP address of the ESP32. Copy/save this for later.

### Server-Side Installation

1. Clone the repo on the Raspberry Pi
```bash
git clone https://github.com/friidryce/UCSD-CSE-118-218-Team-I
```

2. Install the latest version of `Flask`, `nrgok` Python SDK, and `numpy` or alternatively if you have `pip`, run
```bash
pip install -r requirements.txt
```

3. In the `main.py` script, modify the `ESP32` constant appropriately to the local IP address of the ESP32 board.

### Android-Side Installation

1. ...

2. ...

3. Do not build and install the app to the Galaxy Watch just yet.

### How to Run

We require a public forwarding URL so that the Galaxy Watch can send data to our Flask endpoints. Generating a public forwarding URL with `ngrok` will conveniently be automated in our `main.py` script.

Run `python main.py` and copy the forwarding URL outputted.

Modify the forwarding URL in `MainActivity.java` and proceed to building and installing the app to the Galaxy Watch.

Monitor the watch and nanoleaf for color changes! If you do not have a Galaxy Watch, you can simulate sending biometric data to the server using the `server/test/spoof_data.py` script.

> [!Warning]  
> Ensure that the Raspberry Pi and ESP32/Nano Leaf are on the same WiFi network before starting a ngrok session using `main.py`. If you are using the free trial of `ngrok`, you must modify the forwarding URL whenever you re-run the Flask server 

<!------------------------------------------ Network Architecture  ---------------------------------------------------------->
## Network Architecture

![network](server/software_network.png)

<!------------------------------------------ File Architecture  ---------------------------------------------------------->
## File Architecture
```
[UCSD-CSE-118-218-Team-I]
├─ 📂.github/workflows
├─ 📂CSE118_FinalProject
  ├─ 📂app
    ├─ 📂src/main
      ├─ 📂java/com/example/cse118_finalproject
        ├─ 📄MainActivity.java
      ├─ 📂...
      ├─ 📄...
    ├─ 📄build.gradle
    ├─ 📄...
  ├─ 📂...
  ├─ 📄...
├─ 📂esp32_nanoleaf
  ├─ 📂firmware
    ├─ 📂include
      ├─ 📄secrets.h
    ├─ 📂src
      ├─ main.cpp
    ├─ 📂...
    ├─ 📄platformio.ini
  ├─ 📂hardware
    ├─ 📂...
    ├─ 📄...
  ├─ 📄README.md
├─ 📂server
  ├─ 📂test
    ├─ 📄...
  ├─ 📄app.py
├─ 📄.gitignore
├─ 📄README.md
├─ 📄main.py
├─ 📄requirements.txt
```


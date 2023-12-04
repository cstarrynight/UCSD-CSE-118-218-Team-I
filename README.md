<!------------------------------------------ TITLE BLOCK --------------------------------------------------------------->
<h1 align="center"> MoodMesh </h1>

<p align="center">
    CSE 118 Team I
    <br /> <br />
    <a href="https://github.com/friidryce"> Chengzhan Gao </a>
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
- ESP32
- Flask
- PlatformIO
- ngrok

<!------------------------------------------ Getting Started ---------------------------------------------------------->
## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

This project will be running on a Raspberry Pi. Set up your Raspberry Pi by installing the Raspberry Pi OS. If you are comfortable with using Linux, I recommend downloading the Raspberry Pi OS Lite version. Here is a [complete guide for installing the OS](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up).

Make sure you have the latest version of Python 3.11.* on your Raspberry Pi. 

For our wearable app, development and installation was done on [Android Studio](https://developer.android.com/studio) on a personal machine.

Lastly, an optional portion of this project was designing and fabricating a smart light appliance. We prototyped a nano leaf, and the design files and BOM will be listed. The nano leaf is an IoT device, which requires embedded firmware for the ESP32 housed inside. Therefore, we recommend using [Visual Studio Code](https://code.visualstudio.com/) with the [PlatformIO](https://platformio.org/) extension for development.

### Project Installation

1. Clone the repo on the Raspberry Pi
```
git clone https://github.com/friidryce/UCSD-CSE-118-218-Team-I
```

2. Install the latest version of `Flask` or alternatively if you have `pip`, run
```
pip install -r requirements.txt
```

3. Download and setup [ngrok](https://ngrok.com/download). Feel free to use the free trial.

4. Run 

### How to Run

Run `python app.py` while monitoring your wearable app. 

> [!NOTE]  
> Ensure that all your devices, Galaxy Watch, Raspberry Pi, and ESP32/Nano Leaf, are on the same WiFi network.

<!------------------------------------------ File Architecture  ---------------------------------------------------------->
## File Architecture
```
[UCSD-CSE-118-218-Team-I]
├─ 📄.gitignore
├─ 📄README.md
```


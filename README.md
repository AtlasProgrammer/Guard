# Guard Mark III

Simple OpenCV bot for Albion Online, now in Mark III version.

## Attention

This code was created solely for educational purposes and was used to study computer vision libraries and process automation!

**This program is prohibited for distribution.** Anyone involved in its distribution takes full responsibility. Responsibility begins from the moment of receipt of this program.

## Installation

### Requirements

Before installation, ensure that you have the following libraries installed:

- Python 3.x
- OpenCV
- PyAutoGUI
- PyDirectInput
- pywin32
- python-imagesearch

### Installing Libraries

You can install the required libraries using pip. Open the command line and execute the following commands:

```bash
pip install opencv-python
pip install pyautogui
pip install pydirectinput
pip install pywin32
pip install python-imagesearch
```

or

```bash
pip install requirements.txt
```
Cloning the Repository


Download or clone the repository containing the program code:

Verify

Open In Editor run copy code
```bash
git clone https://github.com/AtlasProgrammer/Guard
```
```bash
cd AtlasProgramme
```
Configuration
Recognition Images
Ensure that you have the images required for the program to work. They should be located in the Data folder and include:

- leader.png - image of your character.
- pve.png - image for PvE.
- pvp.png - image for PvP.
- hourse.png - image for interacting with the horse.

Screen Resolution
Make sure that your screen resolution matches the values specified in the Screenshot() function. The current version is set to 1920x1080.

Running the Program

After configuration, you can run the program by executing the following command in the terminal:

Open In Editor run copy code

```bash
python Guard_Mark_III.py
```
### Usage
The program will continuously run in a loop, capturing the screen and performing actions based on detected objects. It will:

### Move the character
- Interact with PvE
- Engage in PvP
- Perform actions with the horse


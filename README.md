# Guard
Simple OpenCV bot for Albion Online

# Attention
This code was created solely for educational purposes and was used to study computer vision libraries and process automation!

# Installation
Requirements
Before installation, ensure that you have the following libraries installed:

Python 3.x
OpenCV
PyAutoGUI
PyDirectInput
pywin32
python-imagesearch
Installing Libraries
You can install the required libraries using pip. Open the command line and execute the following commands:

Open In Editor
Run
Copy code
pip install opencv-python
pip install pyautogui
pip install pydirectinput
pip install pywin32
pip install python-imagesearch
Cloning the Repository
Download or clone the repository containing the program code:

Open In Editor
Run
Copy code
git clone <REPOSITORY_URL>
cd <REPOSITORY_FOLDER>
Configuration
Recognition Images: Ensure that you have the images required for the program to work. They should be located in the Data folder and include:

leader.png - image of your character.
pve.png - image for PvE.
pvp.png - image for PvP.
hourse.png - image for interacting with the horse.
Screen Resolution: Make sure that your screen resolution matches the values specified in the Screenshot() function. The current version is set to 1920x1080.

# Running the Program
After configuration, you can run the program by executing the following command in the terminal:

Open In Editor
Run
Copy code
python <FILENAME>.py
Usage
The program will continuously run in a loop, capturing the screen and performing actions based on detected objects. It will move the character, interact with PvE and PvP, and perform actions with the horse.

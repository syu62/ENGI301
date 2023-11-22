# Ready, Set, Nerds!
This GitHub repository contains the code and software instructions for Ready, Set, Nerds! For information on how to assemble and build the hardware component of the project, please refer to Hackster: https://www.hackster.io/syu62/ready-set-nerds-599477 

## Software
### 1. Package Installation
### 2. SPI Screen and Pin Configuration
Before running any of the LCD code, be sure to configure the pins using "configurepins.sh" and in the terminal type: <br>
`sudo modprobe fbtft_device name=adafruit28 debug=7 verbose=3 gpios=dc:89,reset:26` <br>
`cat /dev/urandom > /dev/fb0` <br>
This should connect your SPI screen and display white noise pixels (like a static tv screen). Then run the LCD-on.sh by typing: <br>
`sudo sh LCD-on.sh` <br>
Your SPI screen should turn black with white text stating "Debian GNU/Linux 10 beaglebone" in the landscape orientation. Afterwards, be sure to download the image "borisLCD.jpg" and run LCD-display,sh by typing: <br>
`sudo sh LCD-display.sh` <br>
This will pull up a sideways image of a pocketbeagle on another screen (this is image borisLCD.jpg). Finally, after ensuring that the SPI screen is working properly, type into the command terminal: <br>
`sudo FRAMEBUFFER=/dev/fb0 startx -- -dpi 60` <br>
This allows tkinter to run the graphics framework and for the SPI screen to disply the tkinter GUI that pops up when run in VIsual Studio Code. Then, in a new terminal, run "GUI.py". This will pull up the Welcome Screen with the Start Game and Instructions button. As of now, however, the touch screen doesn't work so it will remain at the start screen until that feature is established.

### 3. Running the Code
**SetGameCodeOnly.py**
This python file contains the code for only the game Set and its logisitics (it does not include code on connecting tkinter's interface to the SPI screen or the button press or motor). 
On Visual Studio Code, or a similar platform, import the code and the folder "Set_Cards". This folder contains all 81 possible cards in the deck. Once you do both, run the code and a tkinter GUI should appear in a pop-up window. To click buttons and cards, left-click and to unclick cards, left-click again.

**ButtonMotorCode.py**
This python file should be run on Cloud9 with the PocketBeagle connected. It contains the code and configurations for the button press and motor turn. The code should work so that if you press the button, the motor does a 360 rotation. You may have to adjust the value in time.sleep(xx) on line 143 to finetune your continuous motor to spin exactly 360 degrees. Be sure to also adjust lines 73 and 135 to reflect the servo and button's pins, respectively. To run this code, type in CLoud9's terminal: <br>
`sudo python3 ButtonMotorCode.py`

**LCD-on.sh**
This sh file configures the SPI screen and configurates the pins. Be sure to adjust any pins based on your wirings. For the purposes of how I coded set, this code also rotates the SPI display 90 degrees. To run this code, type in Cloud9's terminal: <br>
`sudo sh LCD-on.sh`

**LCD-display.sh**
This sh file demonstrates the the SPI screen is working and connected to Cloud9. Be sure to download the image, "borisLCD.jpg" prior to running. To run this code, type in Cloud9's terminal: <br>
`sudo sh LCD-display.sh`

**DemonstrationSlideShow.py**
This python file contains the code for the slideshow that is demonstrated in the video on Hackster. It shows what should happen if the touchscreen on the SPI screen was established. Be sure to download the file To run this code, type in Cloud9's terminal: <br>
`sudo python3 DemonstrationSlideshow.py`

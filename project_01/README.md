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

# Ready, Set, Nerds!
This GitHub repository contains the code and software instructions for Ready, Set, Nerds! For information on how to assemble and build the hardware component of the project, please refer to Hackster: https://www.hackster.io/syu62/ready-set-nerds-599477 

## Software
### 1. Package Installation
### 2. SPI Screen and Pin Configuration
Before running any of the LCD code, be sure to configure the pins using "configurepins.sh" and in the terminal type:
`sudo modprobe fbtft_device name=adafruit28 debug=7 verbose=3 gpios=dc:89,reset:26`
`cat /dev/urandom > /dev/fb0`

### 3. Running the Code
**SetGameCodeOnly.py**
This python file contains the code for only the game Set and its logisitics (it does not include code on connecting tkinter's interface to the SPI screen or the button press or motor). 
On Visual Studio Code, or a similar platform, import the code and the folder "Set_Cards". This folder contains all 81 possible cards in the deck. Once you do both, run the code and a tkinter GUI should appear in a pop-up window. To click buttons and cards, left-click and to unclick cards, left-click again.

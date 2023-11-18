"""
--------------------------------------------------------------------------
Demonstration Slideshow Code
--------------------------------------------------------------------------
License:
Copyright 2023 - Sunny Yu
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors
may be used to endorse or promote products derived from this software without
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Demonstration Slideshow Code
This drivers has a slideshow of images that demonstrate how the game would've 
run if the SPI screen was able to recognize touch and control the buttons.

"""

# Import libraries 
import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Label
import time
import os
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

# Set up SPI screen as environment for game display
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0')
    os.environ.__setitem__('DISPLAY', ':0.0')

# Constants
SERVO_PIN = "P1_36"
SERVO_CENTER_DUTY = 7.5

# Global variables
global horizontal_size, vertical_size
horizontal_size = 320
vertical_size = 240

# Functions / Classes
class Button():
    """ Button Class """
    pin             = None
    unpressed_value = None
    pressed_value   = None
    sleep_time      = None
    
    def __init__(self, pin=None):
        """ Initialize variables and set up the button """
        if (pin == None):
            raise ValueError("Pin not provided for Button()")
        else:
            self.pin = pin
        
        # By default the unpressed_value is "1" and the pressed
        # value is "0".  This is done to make it easier to change
        # in the future
        self.unpressed_value = 1
        self.pressed_value   = 0
        
        # By default sleep time is "0.1" seconds
        self.sleep_time      = 0.1

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize Button
        GPIO.setup(self.pin, GPIO.IN) 

    # End def


    def is_pressed(self):
        """ Is the Button pressed?
        
           Returns:  True  - Button is pressed
                     False - Button is not pressed
        """
        return GPIO.input(self.pin) == self.pressed_value

    # End def



def stop_continuous_servo(pin, center_duty):
    PWM.start(pin, center_duty)
    print(f"Continuous servo stopped with duty cycle {center_duty}%. Press Ctrl-C to exit.")


def change_display_screens(old, new):
    # changes the display from image to image 
    new.pack()
    old.pack_forget()
    

# Main script
def main():
    # Intialize Tkinter
    root = Tk()
    root.geometry("320x240")
    root.configure(background="white")
    
    # Create frames and other widgets
    image1_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image1_open = Image.open("SlideShowImages/StartScreen.jpg")
    image1_resize = image1_open.resize((horizontal_size,vertical_size))
    image1_photo = ImageTk.PhotoImage(image1_resize)
    image1_label = tk.Label(image1_frame,image=image1_photo)
    image1_label.place(x=0,y=0)

    image2_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image2_open = Image.open("SlideShowImages/Instructions.jpg")
    image2_resize = image2_open.resize((horizontal_size,vertical_size))
    image2_photo = ImageTk.PhotoImage(image2_resize)
    image2_label = tk.Label(image2_frame,image=image2_photo)
    image2_label.place(x=0,y=0)

    image3_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image3_open = Image.open("SlideShowImages/SeeExamples.jpg")
    image3_resize = image3_open.resize((horizontal_size,vertical_size))
    image3_photo = ImageTk.PhotoImage(image3_resize)
    image3_label = tk.Label(image3_frame,image=image3_photo)
    image3_label.place(x=0,y=0)

    image4_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image4_open = Image.open("SlideShowImages/StartScreen.jpg")
    image4_resize = image4_open.resize((horizontal_size,vertical_size))
    image4_photo = ImageTk.PhotoImage(image4_resize)
    image4_label = tk.Label(image4_frame,image=image4_photo)
    image4_label.place(x=0,y=0)

    image5_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image5_open = Image.open("SlideShowImages/StartCards.jpg")
    image5_resize = image5_open.resize((horizontal_size,vertical_size))
    image5_photo = ImageTk.PhotoImage(image5_resize)
    image5_label = tk.Label(image5_frame,image=image5_photo)
    image5_label.place(x=0,y=0)

    image6_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image6_open = Image.open("SlideShowImages/FirstCardSelect.jpg")
    image6_resize = image6_open.resize((horizontal_size,vertical_size))
    image6_photo = ImageTk.PhotoImage(image6_resize)
    image6_label = tk.Label(image6_frame,image=image6_photo)
    image6_label.place(x=0,y=0)

    image7_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image7_open = Image.open("SlideShowImages/SecondCardSelect.jpg")
    image7_resize = image7_open.resize((horizontal_size,vertical_size))
    image7_photo = ImageTk.PhotoImage(image7_resize)
    image7_label = tk.Label(image7_frame,image=image7_photo)
    image7_label.place(x=0,y=0)

    image8_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image8_open = Image.open("SlideShowImages/ThirdCardSelect.jpg")
    image8_resize = image8_open.resize((horizontal_size,vertical_size))
    image8_photo = ImageTk.PhotoImage(image8_resize)
    image8_label = tk.Label(image8_frame,image=image8_photo)
    image8_label.place(x=0,y=0)

    image9_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image9_open = Image.open("SlideShowImages/YesSetRefresh.jpg")
    image9_resize = image9_open.resize((horizontal_size,vertical_size))
    image9_photo = ImageTk.PhotoImage(image9_resize)
    image9_label = tk.Label(image9_frame,image=image9_photo)
    image9_label.place(x=0,y=0)

    image10_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image10_open = Image.open("SlideShowImages/NewCardsButton.jpg")
    image10_resize = image10_open.resize((horizontal_size,vertical_size))
    image10_photo = ImageTk.PhotoImage(image10_resize)
    image10_label = tk.Label(image10_frame,image=image10_photo)
    image10_label.place(x=0,y=0)

    image11_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image11_open = Image.open("SlideShowImages/NewCardsUpdate.jpg")
    image11_resize = image11_open.resize((horizontal_size,vertical_size))
    image11_photo = ImageTk.PhotoImage(image11_resize)
    image11_label = tk.Label(image11_frame,image=image11_photo)
    image11_label.place(x=0,y=0)

    image12_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image12_open = Image.open("SlideShowImages/FirstCardSelect2.jpg")
    image12_resize = image12_open.resize((horizontal_size,vertical_size))
    image12_photo = ImageTk.PhotoImage(image12_resize)
    image12_label = tk.Label(image12_frame,image=image12_photo)
    image12_label.place(x=0,y=0)

    image13_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image13_open = Image.open("SlideShowImages/SecondCardSelect2.jpg")
    image13_resize = image13_open.resize((horizontal_size,vertical_size))
    image13_photo = ImageTk.PhotoImage(image13_resize)
    image13_label = tk.Label(image13_frame,image=image13_photo)
    image13_label.place(x=0,y=0)

    image14_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image14_open = Image.open("SlideShowImages/ThirdCardSelect2.jpg")
    image14_resize = image14_open.resize((horizontal_size,vertical_size))
    image14_photo = ImageTk.PhotoImage(image14_resize)
    image14_label = tk.Label(image14_frame,image=image14_photo)
    image14_label.place(x=0,y=0)

    image15_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image15_open = Image.open("SlideShowImages/YesSetRefresh2.jpg")
    image15_resize = image15_open.resize((horizontal_size,vertical_size))
    image15_photo = ImageTk.PhotoImage(image15_resize)
    image15_label = tk.Label(image15_frame,image=image15_photo)
    image15_label.place(x=0,y=0)

    image16_frame = Frame(root, width=horizontal_size, height=vertical_size, bg="white")
    image16_open = Image.open("SlideShowImages/CongratsScreen.jpg")
    image16_resize = image16_open.resize((horizontal_size,vertical_size))
    image16_photo = ImageTk.PhotoImage(image16_resize)
    image16_label = tk.Label(image16_frame,image=image16_photo)
    image16_label.place(x=0,y=0)


    # begins the slideshow with time for each image to display
    image1_frame.pack()
    root.after(3000, lambda: change_display_screens(image1_frame, image2_frame))
    root.after(6000, lambda: change_display_screens(image2_frame, image3_frame))
    root.after(9000, lambda: change_display_screens(image3_frame, image4_frame))
    root.after(11000, lambda: change_display_screens(image4_frame, image5_frame))
    root.after(15000, lambda: change_display_screens(image5_frame, image6_frame))
    root.after(16000, lambda: change_display_screens(image6_frame, image7_frame))
    root.after(17000, lambda: change_display_screens(image7_frame, image8_frame))
    root.after(18000, lambda: change_display_screens(image8_frame, image9_frame))
    root.after(20000, lambda: change_display_screens(image9_frame, image10_frame))
    root.after(21000, lambda: change_display_screens(image10_frame, image11_frame))
    root.after(24000, lambda: change_display_screens(image11_frame, image12_frame))
    root.after(25000, lambda: change_display_screens(image12_frame, image13_frame))
    root.after(26000, lambda: change_display_screens(image13_frame, image14_frame))
    root.after(27000, lambda: change_display_screens(image14_frame, image15_frame))
    root.after(31000, lambda: change_display_screens(image15_frame, image16_frame))

    
    def check_button_state():
        # waits for button to be pressed for the servo to spin and dispense candy
        button = Button("P2_2") 
        if button.is_pressed:
            stop_continuous_servo(SERVO_PIN, SERVO_CENTER_DUTY)
            time.sleep(0.5)  # Allow time to observe the servo behavior
            stop_continuous_servo(SERVO_PIN, SERVO_CENTER_DUTY)
            PWM.cleanup()
        else:
            # Schedule the function to be called again after 100 milliseconds
            root.after(100, check_button_state)

    # Schedule the initial check after 100 milliseconds
    root.after(33000, check_button_state)
    
    root.mainloop()
    
main()


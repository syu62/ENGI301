"""
--------------------------------------------------------------------------
Button and Motor Driver
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

Button Driver

This driver is built for buttons that have a pull up resistor between the
button and the processor pin (i.e. the input is "High"/"1" when the button is
not pressed) and will be connected to ground when the button is pressed (i.e. 
the input is "Low" / "0" when the button is pressed). When the button is
pressed, that will trigger the continuous motor to rotate 360 degrees.

Software API:

  Button(pin)
    - Provide pin that the button monitors
    
    is_pressed()
      - Return a boolean value (i.e. True/False) on if button is pressed
      - Function consumes no time
    
    wait_for_press(function=None)
      - Wait for the button to be pressed 
      - Optionally takes in an argument "function" which is the function 
        to be executed when waiting for the button to be pressed
      - Function consumes time
      - Returns a tuple:  
        (<time button was pressed>, <data returned by the "function" argument>)
  Motor 
    stop_continuous_servo
      - stops the servo after a certain amount of time
      - time is tweaked to allow the servo to spin only 360 degrees and then stop
  

"""

# import libraries
import time
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

# Constants
SERVO_PIN = "P1_36"
SERVO_CENTER_DUTY = 7.5

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


# Main script
if __name__ == '__main__':
    # sees if the button is pressed and then rotates the continuous servo motor if yes
    # Create instantiation of the button
    button = Button("P2_2") # put GPIO pin of button 
    import time
    
    try:
        while True: 
            if button.is_pressed():
                print("    {0}".format(button.is_pressed()))
                stop_continuous_servo(SERVO_PIN, SERVO_CENTER_DUTY)
                time.sleep(0.5)  # Allow time to observe the servo behavior
                break
    except KeyboardInterrupt:
        pass
    
    finally:
        stop_continuous_servo(SERVO_PIN, SERVO_CENTER_DUTY)
        PWM.cleanup()

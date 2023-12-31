# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blink_USR3
--------------------------------------------------------------------------
Authors: Sunny Yu (sy62@rice.edu)
License:   
Copyright 2023 - Sunny Yu

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Program that will use the Adafruit BBIO library to blink the USR3 LED at
5 Hz (i.e 5 full on/off cycles per second). 

--------------------------------------------------------------------------
"""

#import statements
import Adafruit_BBIO.GPIO as GPIO
import time

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

#setting up all of the USRs on the pocketbeagle

for i in range(4):
    GPIO.setup("USR%d" % i, GPIO.OUT)
    
#end def


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

#while loop to blink USR3 at frequency of 5 Hz
while True:
   #while the file runs, the LED will turn on for 0.1 of a second
   GPIO.output("USR%d" % i, GPIO.HIGH)
   time.sleep(0.1)
   #while the file runs, after 0.1 of a second of the LED turning on,
   #it will turn off
   GPIO.output("USR%d" % i, GPIO.LOW)
   time.sleep(0.1)
   
#end def

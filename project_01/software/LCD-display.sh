"""
--------------------------------------------------------------------------
LCD Display
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

LCD Display

This code is built to demonstrate that the SPI screen is working and connceted 
to Cloud9. After running, the SPI screen should display an image of PocketBeagle.
Make sure to download "borisLCD.jpg" before running.

"""

export FRAMEBUFFER=/dev/fb0
cd images

# Display an image
fbi -noverbose -T 1 -a borisLCD.jpg
# Cycle between several images
# fbi -t 5 -blend 1000 -noverbose -T 1 -a Matthias.jpg Malachi.jpg Alan.jpg Louis.jpg

# Play a movie
# SDL_VIDEODRIVER=fbcon 
# SDL_FBDEV=/dev/fb0
# mplayer -vf-add rotate=4 -framedrop hst_1.mpg

# Look at the framebuffer settings
fbset

# cat /sys/bus/iio/devices/iio:device0/in_voltage5_raw1571

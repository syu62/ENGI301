"""
--------------------------------------------------------------------------
LCD On
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

LCD On

This code connects the SPI screen and configurates the pins required for the
screen to function properly. It also rotates the screen by 90 degrees since
Set was built to be played in lanscape.

"""

# Connect the display before running this.
export LED=51         # P9_16

# This is for the Black SPI 0
export RESET=26     # RESET - P9_20
export DC=89        # D/C   - P9_19
export CS=5         # CS    - P9_17
export BUS=0        # SPI bus 0
# This is for the Black SPI 1
# export RESET=117    # RESET - P9_25
# export DC=115       # D/C   - P9_27
# export CS=113       # CS    - P9_28
# export BUS=1        # SPI bus 1
# This is for the AI SPI 2 & 3
# export RESET=177    # RESET - P9_25
# export DC=111       # D/C   - P9_27
# export CS=207       # CS    - P9_28
# export BUS=2        # SPI bus 2 or 3
# This is for the Pocket SPI 0
# export RESET=57     # RESET - P2.06
# export DC=58        # D/C   - P2.04
# export CS=5         # CS    - P1.06
# export BUS=0        # SPI bus 0

echo SPI $BUS

sudo bash << EOF
    # Remove the framebuffer modules
    if lsmod | grep -q 'fbtft_device ' ; then rmmod fbtft_device;  fi
    if lsmod | grep -q 'fb_ili9341 '   ; then rmmod --force fb_ili9341;    fi
    if lsmod | grep -q 'fbtft '        ; then rmmod --force fbtft;         fi

    # Set the pinmuxes for the display
    # Black SPI 0
    config-pin P1_04 gpio   # D/C
    config-pin P1_34 gpio   # RESET
    config-pin P1_12 spi    # spi 0_d1 MOSI
    config-pin P1_10 spi    # spi 0_d0 MISO
    config-pin P1_08 spi_sclk # spi 0_sclk
    config-pin P1_06 spi_cs # spi 0_cs0
    
    # Black SPI 1
    # config-pin P9_27 gpio   # D/C
    # config-pin P9_25 gpio   # RESET
    # config-pin P9_30 spi    # spi 1_d1 MOSI
    # config-pin P9_29 spi    # spi 1_d0 MISO
    # config-pin P9_31 spi_sclk # spi 1_sclk
    # config-pin P9_28 spi_cs # spi 1_cs0

    # LED pin, turn on
    #./LCD-backlight.py
    
    sleep 0.1
    
    # Insert the framebuffer modules
    # Change busnum to the SPI bus number
    modprobe fbtft_device name=adafruit28 busnum=$BUS rotate=90 gpios=reset:$RESET,dc:$DC cs=0

    # Turn off cursor
    while [ ! -e /dev/fb0 ]
    do
      echo Waiting for /dev/fb0
      sleep 1
    done

    # echo 0 > /sys/class/graphics/fbcon/cursor_blink 

EOF

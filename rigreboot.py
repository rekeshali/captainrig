#!/usr/bin/python3
import sys
from gpiozero import LED
from time import sleep

def press(pin):
    button = LED(pin)
    button.on()
    sleep(1)
    button.off()

def longPress(pin):
    button = LED(pin)
    button.on()
    sleep(8)
    button.off()

def reboot(pin,wait):
    # Shutdown 
    longPress(pin)

    # Wait for cooldown
    sleep(wait)

    # Startup
    press(pin)
    
def rebootHighwind(wait):
    reboot(17,wait)

def rebootTrailblazer(wait):
    reboot(18,wait)

def bootHighwind():
    press(17)

def bootTrailblazer():
    press(18)

if __name__ == "__main__":
    if len(sys.argv)>1:
        arg = sys.argv[1]
        if arg.lower() == 'h':
            rebootHighwind(10)
        elif arg.lower() == 't':
            rebootTrailblazer(10)

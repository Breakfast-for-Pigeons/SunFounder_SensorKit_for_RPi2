#!/usr/bin/env python
"""
Controls the SunFounder tilt switch module.

Use the tilt switch to change the color of an LED.

This program was written on a Raspberry Pi using the Geany IDE.
"""
from gpiozero import PWMLED, Button

tilt_switch = Button(17)
red = PWMLED(pin=18, active_high=True, initial_value=0, frequency=100)
green = PWMLED(pin=27, active_high=True, initial_value=0, frequency=100)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    tilt_switch.close()
    red.close()
    green.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        while True:
            if tilt_switch.is_pressed:
                red.off()
                green.on()
            else:
                red.on()
    except KeyboardInterrupt:
        stop()

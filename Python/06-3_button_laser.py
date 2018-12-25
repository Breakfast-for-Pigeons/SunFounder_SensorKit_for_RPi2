#!/usr/bin/env python
"""
Controls the SunFounder button module.

A button is pressed to activate the laser module.

DO NOT LOOK DIRECTELY INTO THE LASER!

This program was written on a Raspberry Pi using the Geany IDE.
"""
from gpiozero import Button, OutputDevice

button = Button(17)
laser = OutputDevice(pin=18, active_high=False, initial_value=False)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    button.close()
    laser.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        while True:
            if button.is_pressed:
                laser.on()
            else:
                laser.off()
    except KeyboardInterrupt:
        stop()

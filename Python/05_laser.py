#!/usr/bin/env python
"""
Controls the SunFounder laser module.

DO NOT LOOK DIRECTELY INTO THE LASER!

This program was written on a Raspberry Pi using the Geany IDE.
"""

from time import sleep
from gpiozero import OutputDevice

laser = OutputDevice(pin=17, active_high=True, initial_value=False)


def activate_laser():
    """
    Turns the laser on and off
    """
    sleep_speed = 1.0

    while True:
        print("laser on...")
        laser.on()
        sleep(sleep_speed)
        print("...laser off")
        laser.off()
        sleep(sleep_speed)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    laser.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        activate_laser()
    except KeyboardInterrupt:
        stop()

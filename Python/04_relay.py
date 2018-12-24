#!/usr/bin/env python
"""
Controls the SunFounder relay module.

This program was written on a Raspberry Pi using the Geany IDE.
"""

from time import sleep
from gpiozero import OutputDevice

relay = OutputDevice(pin=17)

def activate_relay():
    """
    Turns the relay on and off
    """
    sleep_speed = 0.5

    while True:
        print("...relay on")
        relay.on()
        sleep(sleep_speed)
        print("relay off...")
        relay.off()
        sleep(sleep_speed)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    relay.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        activate_relay()
    except KeyboardInterrupt:
        stop()

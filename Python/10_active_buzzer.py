#!/usr/bin/env python
"""
Controls the SunFounder active buzzer module.

This program was written on a Raspberry Pi using the Geany IDE.
"""
from time import sleep
from gpiozero import Buzzer

buzzer = Buzzer(pin=17, active_high=True, initial_value=False)


def activate_buzzer():
    """
    Activates the buzzer
    """
    sleep_speed = 0.5

    buzzer.on()
    sleep(sleep_speed)
    buzzer.off()
    sleep(sleep_speed)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    buzzer.off()
    buzzer.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        while True:
            activate_buzzer()
    except KeyboardInterrupt:
        stop()

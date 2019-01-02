#!/usr/bin/env python
"""
Controls the SunFounder photo interupter module.

When the photo interupter switch is activated, it changes the color of
an LED.

This program was written on a Raspberry Pi using the Geany IDE.
"""
from time import sleep
from gpiozero import PWMLED, Button

photo_interupter = Button(pin=17, pull_up=False, bounce_time=200,
                          hold_time=1, hold_repeat=False)
red = PWMLED(pin=18, active_high=True, initial_value=1, frequency=100)
green = PWMLED(pin=27, active_high=True, initial_value=0, frequency=100)


def print_message():
    """
    Prints a message to the screen letting the user know the photo
    interupter was activated.
    """
    print('*************************')
    print('*   Light was blocked   *')
    print('*************************')
    sleep(2)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    photo_interupter.close()
    red.close()
    green.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        while True:
            if photo_interupter.is_pressed:
                red.off()
                green.on()
                print_message()
            else:
                red.on()
    except KeyboardInterrupt:
        stop()

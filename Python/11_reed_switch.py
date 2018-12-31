#!/usr/bin/env python
"""
Controls the SunFounder reed switch module.

When the reed switch is activated, it changes the color of an LED.

This program was written on a Raspberry Pi using the Geany IDE.
"""
from time import sleep
from gpiozero import PWMLED, Button

button = Button(17)
red = PWMLED(pin=18, active_high=True, initial_value=1, frequency=100)
green = PWMLED(pin=27, active_high=True, initial_value=0, frequency=100)


def print_message():
    """
    Prints a message to the screen letting the user know the reed
    switch was activated.
    """
    print('***********************************')
    print('*   Detected Magnetic Material!   *')
    print('***********************************')
    sleep(1)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    button.close()
    red.close()
    green.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        while True:
            if button.is_pressed:
                red.off()
                green.on()
                print_message()
            else:
                red.on()
    except KeyboardInterrupt:
        stop()


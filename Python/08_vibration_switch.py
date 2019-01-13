#!/usr/bin/env python
"""
Controls the SunFounder vibration switch module.

When the vibration switch is activated, it changes the color of an LED.

This program was written on a Raspberry Pi using the Geany IDE.
"""
from time import sleep
from gpiozero import PWMLED, Button

vibration_switch = Button(17)
red = PWMLED(pin=18, active_high=True, initial_value=0, frequency=100)
green = PWMLED(pin=27, active_high=True, initial_value=1, frequency=100)


def print_message():
    """
    Prints a message to the screen letting the user know the vibration
    switch was activated.
    """
    print('***********************************')
    print('*       Detected Vibration!       *')
    print('***********************************')
    sleep(1)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    vibration_switch.close()
    red.close()
    green.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        while True:
            if vibration_switch.is_pressed:
                green.off()
                red.on()
                print_message()
                red.off()
                green.on()
            else:
                green.on()
    except KeyboardInterrupt:
        stop()

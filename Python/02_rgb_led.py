#!/usr/bin/env python
"""
Makes the SunFounder RGB LED change 8 different colors.

This program was written on a Raspberry Pi using the Geany IDE.
"""
from time import sleep
from gpiozero import RGBLED

# NOTE: active_high needs to be set to True for common cathode LEDs and
# set to False for common annode LEDs.
# Page 37 of the Sunfounder Sensor Kit book, it says that it is a 
# common cathode RGBLED, but when I set active_high to True, it didn't
# work properly. I set active_high to False, and it works as expected.
led = RGBLED(red=17, green=18, blue=27, active_high=False,
             initial_value=(0, 0, 0), pwm=True, pin_factory=None)


def cycle_colors():
    """
    Cycles through the 8 main colors.
    """

    sleep_speed = 1

    led.color = (0, 0, 1)  # blue
    sleep(sleep_speed)
    led.color = (0, 1, 0)  # green
    sleep(sleep_speed)
    led.color = (0, 1, 1)  # cyan
    sleep(sleep_speed)
    led.color = (1, 0, 0)  # red
    sleep(sleep_speed)
    led.color = (1, 0, 1)  # magenta
    sleep(sleep_speed)
    led.color = (1, 1, 0)  # yellow
    sleep(sleep_speed)
    led.color = (1, 1, 1)  # white
    sleep(sleep_speed)
    led.color = (0, 0, 0)  # off
    sleep(sleep_speed)


def destroy():
    """
    Closes the LED pins and then exits.
    """
    print("\nStopping program.")
    led.close()
    exit()


if __name__ == "__main__":
    try:
        cycle_colors()
    except KeyboardInterrupt:
        destroy()

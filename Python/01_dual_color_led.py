#!/usr/bin/env python
"""
Makes the SunFounder Dual-Color LED blink red and green.

This program was written on a Raspberry Pi using the Geany IDE.
"""

from time import sleep
from gpiozero import PWMLED

red = PWMLED(pin=17, active_high=True, initial_value=0, frequency=100)
green = PWMLED(pin=18, active_high=True, initial_value=0, frequency=100)


def loop():
    """
    Turns the red light on and off, then turns the green light on and off.
    """

    while True:
        red_blink()
        green_blink()
        red_pulse()
        green_pulse()
        orange_led()


def red_blink():
    """
    Red LED blinks 3 times
    """
    red.value = 1.0
    sleep_speed = 1.0   # one second

    red.blink(on_time=1, off_time=1, fade_in_time=0,
              fade_out_time=0, n=3, background=False)
    sleep(sleep_speed)


def green_blink():
    """
    Green LED blinks 3 times
    """
    green.value = 1.0
    sleep_speed = 1.0   # one second

    green.blink(on_time=1, off_time=1, fade_in_time=0,
                fade_out_time=0, n=3, background=False)
    sleep(sleep_speed)


def red_pulse():
    """
    Pulses red LED 3 times
    """
    red.value = 1.0
    sleep_speed = 1.0   # one second

    red.pulse(fade_in_time=1, fade_out_time=1,
              n=3, background=False)
    sleep(sleep_speed)


def green_pulse():
    """
    Pulses green LED 3 times
    """
    green.value = 1.0
    sleep_speed = 1.0   # one second

    green.pulse(fade_in_time=1, fade_out_time=1,
                n=3, background=False)
    sleep(sleep_speed)


def orange_led():
    """
    Modifies the red and green values to change the color.
    """

    sleep_speed = 0.5   # one second

    red.value = 0.05
    green.value = 1.0
    sleep(sleep_speed)
    red.value = 0.10
    sleep(sleep_speed)
    red.value = 0.15
    sleep(sleep_speed)
    red.value = 0.20
    sleep(sleep_speed)
    red.value = 0.25
    sleep(sleep_speed)
    red.value = 0.30
    sleep(sleep_speed)
    red.value = 0.35
    sleep(sleep_speed)
    red.value = 0.40
    sleep(sleep_speed)
    red.value = 0.45
    sleep(sleep_speed)
    red.value = 0.50
    sleep(sleep_speed)
    red.value = 0.55
    sleep(sleep_speed)
    red.value = 0.60
    sleep(sleep_speed)
    red.value = 0.65
    sleep(sleep_speed)
    red.value = 0.70
    sleep(sleep_speed)
    red.value = 0.75
    sleep(sleep_speed)
    red.value = 0.80
    sleep(sleep_speed)
    red.value = 0.85
    sleep(sleep_speed)
    red.value = 0.90
    sleep(sleep_speed)
    red.value = 0.95
    sleep(sleep_speed)
    red.value = 1.00
    sleep(sleep_speed)
    green.value = 0.0
    red.value = 0.0
    sleep(sleep_speed)


def destroy():
    """
    Closes the LED pins and then exits.
    """
    print("\nStopping program.")
    red.close()
    green.close()
    exit()


if __name__ == "__main__":
    print("Press Crtl-C to stop the program.")
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

#!/usr/bin/env python
"""
This program was written for the SunFounder Dual-Color LED module.

....................

Functions:

- activate_led: the main function
- red_blink: makes the red LED blink
- green_blink: makes the green LED blink
- red_pulse: makes the red LED pulse
- green_pulse: makes the green LED pulse
- orange_led: modifies the values of red and gree to make the LED turn
              an orange color.
- stop: Prints a message and closes the resources used by the LED.

....................

This program was written on a Raspberry Pi using the Geany IDE.
"""

from time import sleep
from gpiozero import PWMLED

red = PWMLED(pin=17, active_high=True, initial_value=0, frequency=100)
green = PWMLED(pin=18, active_high=True, initial_value=0, frequency=100)


def activate_led():
    """
    Turns the red light on and off, then turns the green light on and off.
    """
    sleep_speed = 1.0   # one second

    while True:
        red_blink()
        sleep(sleep_speed)
        green_blink()
        sleep(sleep_speed)
        red_pulse()
        sleep(sleep_speed)
        green_pulse()
        sleep(sleep_speed)
        orange_led()
        sleep(sleep_speed)


def red_blink():
    """
    Makes the red LED blink

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    red.value = 1.0

    red.blink(on_time=1, off_time=1, fade_in_time=0,
              fade_out_time=0, n=3, background=False)


def green_blink():
    """
    Makes the green LED blink

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    green.value = 1.0

    green.blink(on_time=1, off_time=1, fade_in_time=0,
                fade_out_time=0, n=3, background=False)


def red_pulse():
    """
    Makes the red LED pulse

    The number of times it pulses can be changed by editing the value
    of 'n'.

    The duration of the pulse can be changed by editing the fade_in_time
    and fade_out_time values. I set the default for each of them to 1,
    which means the LED brightness fades in for 1 second and then fades
    out for one second.
    """
    red.value = 1.0

    red.pulse(fade_in_time=1, fade_out_time=1,
              n=3, background=False)


def green_pulse():
    """
    Makes the green LED pulse

    The number of times it pulses can be changed by editing the value
    of 'n'.

    The duration of the pulse can be changed by editing the fade_in_time
    and fade_out_time values. I set the default for each of them to 1,
    which means the LED brightness fades in for 1 second and then fades
    out for one second.
    """
    green.value = 1.0

    green.pulse(fade_in_time=1, fade_out_time=1,
                n=3, background=False)


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


def stop():
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
        activate_led()
    except KeyboardInterrupt:
        stop()

#!/usr/bin/env python
"""
This program was written for the SunFounder RGB LED module.

....................

Functions:

- cycle_leds: Cycles through the 7 main colors.
- blink_blue: Sets the RGB LED to blue and blinks.
- blink_green: Sets the RGB LED to green and blinks.
- blink_cyan: Sets the RGB LED to cyan and blinks.
- blink_red: Sets the RGB LED to red and blinks.
- blink_magenta: Sets the RGB LED to magenta and blinks.
- blink_yellow: Sets the RGB LED to yellow and blinks.
- blink_white: Sets the RGB LED to cyan and blinks.
- christmas_lights: the LED blinks red and green
- pulse_blue: Sets the RGB LED to blue and pulses.
- pulse_green: Sets the RGB LED to green and pulses.
- pulse_cyan: Sets the RGB LED to cyan and pulses.
- pulse_red: Sets the RGB LED to red and pulses.
- pulse_magenta: Sets the RGB LED to magenta and pulses.
- pulse_yellow: Sets the RGB LED to yellow and pulses.
- pulse_white: Sets the RGB LED to cyan and pulses.
- stop: Prints a message and closes the resources used by the LED.

....................

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
    Cycles through the 7 main colors.
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


def blink_blue():
    """
    Sets the RGB LED to blue and blinks.

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
              on_color=(0, 0, 1), off_color=(0, 0, 0), n=3,
              background=False)


def blink_green():
    """
    Sets the RGB LED to green and blinks.

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
              on_color=(0, 1, 0), off_color=(0, 0, 0), n=3,
              background=False)


def blink_cyan():
    """
    Sets the RGB LED to cyan and blinks.

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
              on_color=(0, 1, 1), off_color=(0, 0, 0), n=3,
              background=False)


def blink_red():
    """
    Sets the RGB LED to red and blinks.

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
              on_color=(1, 0, 0), off_color=(0, 0, 0), n=3,
              background=False)


def blink_magenta():
    """
    Sets the RGB LED to magenta and blinks.

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
              on_color=(1, 0, 1), off_color=(0, 0, 0), n=3,
              background=False)


def blink_yellow():
    """
    Sets the RGB LED to yellow and blinks.

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
              on_color=(1, 1, 0), off_color=(0, 0, 0), n=3,
              background=False)


def blink_white():
    """
    Sets the RGB LED to white and blinks.

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
              on_color=(1, 1, 1), off_color=(0, 0, 0), n=3,
              background=False)


def christmas_lights():
    """
    Makes the RGB LED alternate between red and green.

    The number of times it blinks can be changed by editing the value
    of 'n'.

    The duration of the blink can be changed by editing the on_time and
    off_time values. I set the default for each of them to 1, which
    means the LED stays on for 1 second and then turns off for one
    second.
    """
    led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
              on_color=(1, 0, 0), off_color=(0, 1, 0), n=5,
              background=False)


def pulse_blue():
    """
    Sets the RGB LED to blue and pulses.

    The number of times it pulses can be changed by editing the value
    of 'n'.

    The duration of the pulse can be changed by editing the fade_in_time
    and fade_out_time values. I set the default for each of them to 1,
    which means the LED brightness fades in for 1 second and then fades
    out for one second.
    """
    led.pulse(fade_in_time=1, fade_out_time=1, on_color=(0, 0, 1),
              off_color=(0, 0, 0), n=3, background=False)


def pulse_green():
    """
    Sets the RGB LED to green and pulses.

    The number of times it pulses can be changed by editing the value
    of 'n'.

    The duration of the pulse can be changed by editing the fade_in_time
    and fade_out_time values. I set the default for each of them to 1,
    which means the LED brightness fades in for 1 second and then fades
    out for one second.
    """
    led.pulse(fade_in_time=1, fade_out_time=1, on_color=(0, 1, 0),
              off_color=(0, 0, 0), n=3, background=False)


def pulse_cyan():
    """
    Sets the RGB LED to cyan and pulses.

    The number of times it pulses can be changed by editing the value
    of 'n'.

    The duration of the pulse can be changed by editing the fade_in_time
    and fade_out_time values. I set the default for each of them to 1,
    which means the LED brightness fades in for 1 second and then fades
    out for one second.
    """
    led.pulse(fade_in_time=1, fade_out_time=1, on_color=(0, 1, 1),
              off_color=(0, 0, 0), n=3, background=False)


def pulse_red():
    """
    Sets the RGB LED to red and pulses.

    The number of times it pulses can be changed by editing the value
    of 'n'.

    The duration of the pulse can be changed by editing the fade_in_time
    and fade_out_time values. I set the default for each of them to 1,
    which means the LED brightness fades in for 1 second and then fades
    out for one second.
    """
    led.pulse(fade_in_time=1, fade_out_time=1, on_color=(1, 0, 0),
              off_color=(0, 0, 0), n=3, background=False)


def pulse_magenta():
    """
    Sets the RGB LED to magenta and pulses.

    The number of times it pulses can be changed by editing the value
    of 'n'.

    The duration of the pulse can be changed by editing the fade_in_time
    and fade_out_time values. I set the default for each of them to 1,
    which means the LED brightness fades in for 1 second and then fades
    out for one second.
    """
    led.pulse(fade_in_time=1, fade_out_time=1, on_color=(1, 0, 1),
              off_color=(0, 0, 0), n=3, background=False)


def pulse_yellow():
    """
    Sets the RGB LED to yellow and pulses.

    The number of times it pulses can be changed by editing the value
    of 'n'.

    The duration of the pulse can be changed by editing the fade_in_time
    and fade_out_time values. I set the default for each of them to 1,
    which means the LED brightness fades in for 1 second and then fades
    out for one second.
    """
    led.pulse(fade_in_time=1, fade_out_time=1, on_color=(1, 1, 0),
              off_color=(0, 0, 0), n=3, background=False)


def pulse_white():
    """
    Sets the RGB LED to white and pulses.

    The number of times it pulses can be changed by editing the value
    of 'n'.

    The duration of the pulse can be changed by editing the fade_in_time
    and fade_out_time values. I set the default for each of them to 1,
    which means the LED brightness fades in for 1 second and then fades
    out for one second.
    """
    led.pulse(fade_in_time=1, fade_out_time=1, on_color=(1, 1, 1),
              off_color=(0, 0, 0), n=3, background=False)


def stop():
    """
    Closes the LED pins and then exits.
    """
    print("\nStopping program.")
    led.close()
    exit()


if __name__ == "__main__":
    try:
        cycle_colors()
        blink_blue()
        blink_green()
        blink_cyan()
        blink_red()
        blink_magenta()
        blink_yellow()
        blink_white()
        christmas_lights()
        pulse_blue()
        pulse_green()
        pulse_cyan()
        pulse_red()
        pulse_magenta()
        pulse_yellow()
        pulse_white()
    except KeyboardInterrupt:
        stop()

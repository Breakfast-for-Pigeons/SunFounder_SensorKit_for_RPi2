#!/usr/bin/env python
"""
Controls the SunFounder reed switch module.

When the reed switch is activated, it changes the color of an LED.

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import files                                #
########################################################################
from time import sleep
from gpiozero import PWMLED, Button
import pygame

########################################################################
#                           Variables                                  #
########################################################################

reed_switch = Button(17)
red = PWMLED(pin=18, active_high=True, initial_value=0, frequency=100)
green = PWMLED(pin=27, active_high=True, initial_value=0, frequency=100)

########################################################################
#                           Initialize                                 #
########################################################################

pygame.mixer.init()

########################################################################
#                            Functions                                 #
########################################################################


def play_sound_file():
    """
    Plays a message to let the user know the reed
    switch was activated.
    """
    sound_file = 'Sounds/magnetic_field_detected.ogg'

    pygame.mixer.music.load(sound_file)     # Loads the sound file
    pygame.mixer.music.play()               # Plays the sound file
    sleep(3)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    reed_switch.close()
    red.close()
    green.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        while True:
            if reed_switch.is_pressed:
                red.off()
                green.on()
                play_sound_file()
                green.off()
                red.on()
            else:
                red.on()
    except KeyboardInterrupt:
        stop()

#!/usr/bin/env python
"""
Controls the SunFounder button module.

A button is pressed to activate the laser module.

DO NOT LOOK DIRECTELY INTO THE LASER!

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import files                                #
########################################################################
from time import sleep
from gpiozero import Button, OutputDevice
import pygame

########################################################################
#                           Variables                                  #
########################################################################

button = Button(17)
laser = OutputDevice(pin=18, active_high=False, initial_value=False)


########################################################################
#                           Initialize                                 #
########################################################################

pygame.mixer.init()

########################################################################
#                            Functions                                 #
########################################################################


def play_sound_file():
    """
    Plays a message to let the user know the vibration
    switch was activated.
    """
    sound_file = 'Sounds/laser_activated.ogg'

    pygame.mixer.music.load(sound_file)     # Loads the sound file
    pygame.mixer.music.play()               # Plays the sound file
    sleep(3)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    button.close()
    laser.close()
    exit()


if __name__ == '__main__':
    print("Press Crtl-C to stop the program.")
    try:
        while True:
            if button.is_pressed:
                laser.on()
                play_sound_file()
            else:
                laser.off()
    except KeyboardInterrupt:
        stop()

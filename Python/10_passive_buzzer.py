#!/usr/bin/env python
"""
-----------------------------------------------------

  This is a program for the Sunfounder passive buzzer module.
  It will play simple songs.
  You could try to make songs by youselves!

        Passive buzzer             Pi
            VCC ----------------- 3.3V
            GND ------------------ GND
            SIG ---------------- Pin 11

-----------------------------------------------------
"""
from time import sleep
from gpiozero import PWMOutputDevice

buzzer = PWMOutputDevice(pin=17, active_high=True, initial_value=0.5,
                         frequency=440)

CL = [0, 131, 147, 165, 175, 196, 211, 248]  # Frequency of Low C notes

CM = [0, 262, 294, 330, 350, 393, 441, 495]  # Frequency of Middle C notes

CH = [0, 525, 589, 661, 700, 786, 882, 990]  # Frequency of High C notes

# Notes of song1
song_1 = [CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6],
          CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
          CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
          CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]]

# Beats of song 1, 1 means 1/8 beats
beat_1 = [1, 1, 3, 1, 1, 3, 1, 1,
          1, 1, 1, 1, 1, 1, 3, 1,
          1, 3, 1, 1, 1, 1, 1, 1,
          1, 2, 1, 1, 1, 1, 1, 1,
          1, 1, 3]

# Notes of song2
song_2 = [CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1],
          CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
          CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
          CM[3], CM[2], CL[5], CL[7], CM[2], CM[1]]

# Beats of song 2, 1 means 1/8 beats
beat_2 = [1, 1, 2, 2, 1, 1, 2, 2,
          1, 1, 2, 2, 1, 1, 3, 1,
          1, 2, 2, 1, 1, 2, 2, 1,
          1, 2, 2, 1, 1, 3]


def passive_buzzer():
    """
    Plays songs on the active buzzer
    """
    while True:
        print("\nPlaying song 1...")
        # Play song 1
        for i in range(1, len(song_1)):
            # Change the frequency along the song note
            buzzer.frequency = song_1[i]
            # delay a note for beat * 0.5s
            sleep(beat_1[i] * 0.5)
        # Wait a second for next song.
        sleep(1)

        print("\nPlaying song 2...")
        # Play song 2
        for i in range(1, len(song_2)):
            # Change the frequency along the song note
            buzzer.frequency = song_2[i]
            # delay a note for beat * 0.5s
            sleep(beat_2[i] * 0.5)
        # Wait a second for next song.
        sleep(1)


def stop():
    """
    Releases resources and exits.
    """
    print("\nStopping program.")
    buzzer.off()
    buzzer.close()
    exit()


if __name__ == '__main__':      # Program start from here
    try:
        passive_buzzer()
    # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    except KeyboardInterrupt:
        stop()

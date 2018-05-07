#!/usr/bin/env python3
"""
The  DIGITAL SENSORS   workshop.
Also covers the ev3.Sound, ev3.Leds, and ev3.Screen classes.

Person 1: ev3.TouchSensor
Person 2: ev3.Button
Person 3: ev3.RemoteControl

Authors: David Fisher, David Mutchler and JUN FAN.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# DONE: 2.  WITH YOUR INSTRUCTOR, discuss the "big picture" of this project,
#           as described in the   _README_FIRST.txt   file.
#
# When your   ** ENTIRE TEAM ** understands that:
#
#      -- Each of you works in your own "person" file.
#      -- Each of you has different tasks.
#      -- The tasks that each of you do are ALMOST EXACTLY THE SAME.
#           - So, HELP EACH OTHER!
#           - As you finish each TO-DO, check that your teammates are doing OK!
#
# change this TO-DO to DONE.
# -----------------------------------------------------------------------------

import ev3dev.ev3 as ev3
import time
from PIL import Image


def main():
    """ Calls the   TEST   functions in this module. """
    # Uncomment these tests as you proceed through this module.

    run_test_touch_sensor()
    run_test_wait_for_press()
    run_test_show_images()


def run_test_touch_sensor():
    """ Tests the   print_state_of_touch_sensor   function. """
    print()
    print('-----------------------------------------------------')
    print('Testing the   print_state_of_touch_sensor   function:')
    print('-----------------------------------------------------')

    print()
    print('Test 1:')
    print('  First, locate the TOUCH sensor on the robot.  Get help as needed.')

    print()
    print('  Then, ask someone to help you by PRESSING and RELEASING')
    print('  the TOUCH sensor during this test run.')
    print('  Get that person ready to go, and THEN:')
    print()
    input('Press ENTER on your keyboard when your friend'
          + ' is READY to PRESS/RELEASE the TOUCH sensor:')

    print()
    print('QUICK: Ask your friend to repeatedly'
          + ' PRESS and RELEASE the TOUCH sensor now!')
    print('This test should run for about 5 seconds.')
    print_state_of_touch_sensor(10, 0.5)

    print()
    print('The test SUCCEEDED if 10 0s and 1s'
          + ' were printed on the SSH terminal window,')
    print('at intervals of about 0.5 seconds each, with your code printing:')
    print('   1   when your friend was PRESSING the TOUCH sensor')
    print('   0   when your friend was NOT pressing the TOUCH sensor')

    print()
    print('Test 2:')
    print('  Let\'s try again once more.')
    print('  As before, ask your friend to GET READY.')
    print('  This time, your friend should PRESS/RELEASE'
          + ' ** quickly ** during the test.')
    print()
    input('Press ENTER on your keyboard when your friend is'
          + ' READY to PRESS/RELEASE the TOUCH sensor:')

    print()
    print('QUICK: Ask your friend to repeatedly'
          + ' PRESS and RELEASE the TOUCH sensor now!')
    print('This test should run for about 5 seconds.')
    print_state_of_touch_sensor(100, 0.05)

    print()
    print('The test SUCCEEDED if 100 0s and 1s'
          + ' were printed on the SSH terminal window,')
    print('at intervals of about 0.05 seconds each, with your code printing:')
    print('   1   when your friend was PRESSING the TOUCH sensor')
    print('   0   when your friend was NOT pressing the TOUCH sensor')
    print('Note: Each sensor read may take a bit more than 0.05 second,'
          + ' so the total time may be more than 5 seconds.')
    print()


def print_state_of_touch_sensor(n, seconds_per_print):
    """
    Constructs an ev3.TouchSensor object.
    Then does the following  n  times (where n is the first argument):
       1. Prints the STATE of the touch sensor.
       2. SLEEPs for the given number of seconds.
    """

    touch_sensor = ev3.TouchSensor()

    for k in range(n):
        print(touch_sensor.is_pressed)
        time.sleep(seconds_per_print)

    # -------------------------------------------------------------------------
    # DONE: 3.  Implement and test this function.
    #           Tests have been written for you (above).
    # -------------------------------------------------------------------------


def run_test_wait_for_press():
    """ Tests the   wait_for_press   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   wait_for_press   function:')
    print('--------------------------------------------------')

    print('Test:')
    print('  First, locate the TOUCH sensor on the robot.  Get help as needed.')
    print('  Then, ask someone to help you by PRESSING the TOUCH sensor'
          + ' WHEN YOU SAY TO DO SO.')

    print()
    print('  Get that person ready to go, and THEN:')
    print()
    input('Press ENTER on your keyboard, wait a bit and THEN ask'
          + ' your friend to press the touch sensor.')

    print()
    print('TAKE YOUR TIME!  Whenever you wish, ask your friend'
          + ' to press the touch sensor (if you have not already done so.')
    print()
    wait_for_press()

    print()
    print('The test succeeded if  *** NOTHING happened ***')
    print('  ***  UNTIL your friend PRESSED the touch sensor.  ***')
    print()


def wait_for_press():
    """
    Constructs an ev3.TouchSensor object.
    Then repeatedly:
       1. Gets the STATE of the touch sensor
            and leaves the loop if that state is 1
            (i.e., when the touch sensor is pressed).
       2. Sleeps for a small amount (say, 0.05 seconds).
    """

    touch_sensor = ev3.TouchSensor()

    while True:
        if touch_sensor.is_pressed:
            break
        time.sleep(0.05)

    # -------------------------------------------------------------------------
    # DONE: 4.  Implement and test this function.
    #           Tests have been written for you (above).
    # -------------------------------------------------------------------------


def run_test_show_images():
    """ Tests the   show_images   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   show_images   function:')
    print('--------------------------------------------------')

    # All of these images are exactly 178 by 128 pixels, which is the exact
    # screen resolution of the BRICK.  They are made by Lego and ship
    # with the Lego Mindstorm EV3 Home Edition software.

    eyes = \
        "/home/robot/csse120/assets/images/ev3_lego/eyes_neutral.bmp"
    angry_eyes = \
        "/home/robot/csse120/assets/images/ev3_lego/eyes_angry.bmp"
    puppy_dog_eyes = \
        "/home/robot/csse120/assets/images/ev3_lego/eyes_disappointed.bmp"
    sad_eyes = \
        "/home/robot/csse120/assets/images/ev3_lego/eyes_hurt.bmp"
    shifty_eyes = \
        "/home/robot/csse120/assets/images/ev3_lego/eyes_pinch_left.bmp"
    progress_0 = \
        "/home/robot/csse120/assets/images/ev3_lego/progress_bar_0.bmp"
    progress_50 = \
        "/home/robot/csse120/assets/images/ev3_lego/progress_bar_50.bmp"
    progress_100 = \
        "/home/robot/csse120/assets/images/ev3_lego/progress_bar_100.bmp"
    teary_eyes = \
        "/home/robot/csse120/assets/images/ev3_lego/eyes_tear.bmp"

    # Make Python images (using the PIL library) from the files:
    files = [eyes, angry_eyes, puppy_dog_eyes, sad_eyes, shifty_eyes,
             progress_0, progress_50, progress_100, teary_eyes]
    images = []
    for k in range(len(files)):
        images.append(Image.open(files[k]))

    print()
    input('Press ENTER on your keyboard when you are ready to see images'
          + ' on the **  BRICK\'s  ** screen:')

    print()

    show_images(images)

    print()
    print('Look at the TESTING CODE to see the names of the files')
    print('that contain the IMAGES that you saw.')
    print()


def show_images(list_of_images):
    """
    Constructs an ev3.Screen object and an ev3.TouchSensor object.
    Then, for each image in the given list of images:
       1. Prints "Press the touch sensor for the next image."
       2. Waits for the user to PRESS the touch sensor.
       3. Waits for the user to RELEASE the touch sensor.
       4. Prints "Look at the image on the BRICK!".
       5. Displays the image on the ev3 BRICK's screen.

    Type hints:
      :type list_of_images: []
    """


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

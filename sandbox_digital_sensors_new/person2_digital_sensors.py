#!/usr/bin/env python3
"""
The  DIGITAL SENSORS   workshop.
Also covers the ev3.Sound, ev3.Leds, and ev3.Screen classes.

Person 1: ev3.TouchSensor
Person 2: ev3.Button
Person 3: ev3.RemoteControl

Authors: David Fisher, David Mutchler and Zhiyu Wang.
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


def main():
    """ Calls the   TEST   functions in this module. """
    # Uncomment these tests as you proceed through this module.

    # run_test_buttons_on_brick()
    # run_test_wait_for_press_on_brick_button()
    run_test_show_leds()


def run_test_buttons_on_brick():
    """ Tests the   print_state_of_left_button_on_brick   function. """
    print()
    print('-------------------------------------------------------------')
    print('Testing the   print_state_of_left_button_on_brick   function:')
    print('-------------------------------------------------------------')

    print()
    print('Test 1:')
    print('  First, getting help as needed, locate the following buttons'
          + ' on the ev3 BRICK:')
    print('     The  LEFT      button.')
    print('     The  RIGHT     button.')
    print('     The  UP        button.')
    print('     The  DOWN      button.')
    print('     The  BACKSPACE button.')
    print('  We will not use the  ENTER  button (which is the MIDDLE one).')

    print()
    print('  Then, ask someone to help you by PRESSING and RELEASING')
    print('  the LEFT button on the ev3 BRICK during this test run.')
    print('  Get that person ready to go, and THEN:')
    print()
    input('Press ENTER on your keyboard when your friend'
          + ' is READY to PRESS/RELEASE the LEFT button on the ev3 BRICK:')

    print()
    print('QUICK: Ask your friend to repeatedly'
          + ' PRESS and RELEASE the LEFT button on the ev3 BRICK now!')
    print('This test should run for about 5 seconds.')
    print_state_of_left_button_on_brick(10, 0.5)

    print()
    print('The test SUCCEEDED if 10 10 True\'s and False\'s'
          + ' were printed on the SSH terminal window,')
    print('at intervals of about 0.5 seconds each, with your code printing:')
    print('   True    when your friend was PRESSING the LEFT button'
          + ' on the ev3 BRICK')
    print('   False   when your friend was NOT pressing the LEFT button'
          + ' on the ev3 BRICK')

    print()
    print('Test 2:')
    print('  Let\'s try again once more.')
    print('  As before, ask your friend to GET READY.')
    print('  This time, your friend should PRESS/RELEASE'
          + ' ** quickly ** during the test.')
    print()
    input('Press ENTER on your keyboard when your friend is'
          + ' READY to PRESS/RELEASE the LEFT button on the ev3 BRICK:')

    print()
    print('QUICK: Ask your friend to repeatedly'
          + ' PRESS and RELEASE the LEFT button on the ev3 BRICK now!')
    print('This test should run for about 5 seconds.')
    print_state_of_left_button_on_brick(100, 0.05)

    print()
    print('The test SUCCEEDED if 100 True\'s and False\'s'
          + ' were printed on the SSH terminal window,')
    print('at intervals of about 0.1 seconds each, with your code printing:')
    print('   True    when your friend was PRESSING the LEFT button'
          + ' on the ev3 BRICK')
    print('   False   when your friend was NOT pressing the LEFT button'
          + ' on the ev3 BRICK')
    print('Note: Each sensor read may take a bit more than 0.05 second,'
          + ' so the total time may be more than 5 seconds.')
    print()


def print_state_of_left_button_on_brick(n, seconds_per_print):
    """
    Constructs an ev3.Button object.
    Then does the following  n  times (where n is the first argument):
       1. Prints the STATE of the LEFT button on the ev3 BRICK.
       2. SLEEPs for the given number of seconds.
    """
    # -------------------------------------------------------------------------
    # DONE: 3.  Implement and test this function.
    #           Tests have been written for you (above).
    # -------------------------------------------------------------------------
    button = ev3.Button()
    for k in range(n):
        print(button.left)
        time.sleep(seconds_per_print)


def run_test_wait_for_press_on_brick_button():
    """ Tests the   wait_for_UP_button_press   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   wait_for_UP_button_press   function:')
    print('--------------------------------------------------')

    print('Test:')
    print('  First, getting help as needed, locate the following buttons'
          + ' on the ev3 BRICK:')
    print('     The  LEFT      button.')
    print('     The  RIGHT     button.')
    print('     The  UP        button.')
    print('     The  DOWN      button.')
    print('     The  BACKSPACE button.')
    print('  We will not use the  ENTER  button (which is the MIDDLE one).')

    print()
    print('  In THIS test, we will use the ** UP ** button on the ev3 brick.')
    print()
    print('  So, ask someone to help you by PRESSING the ** UP ** button'
          + ' on the ev3 BRICK WHEN YOU SAY TO DO SO.')

    print()
    print('  Get that person ready to go, and THEN:')
    print()
    input('Press ENTER on your keyboard, wait a bit and THEN ask your friend\n'
          + 'FIRST to press the LEFT, RIGHT, and DOWN buttons'
          + 'on the ev3 BRICK\n'
          + 'and only THEN to press the ** UP ** button.')

    print()
    print('TAKE YOUR TIME!  Whenever you wish,'
          + ' if you have not already done so,')
    print(' ask your friend FIRST to press the LEFT, RIGHT, and DOWN buttons')
    print('and only THEN to press the  ** UP **  button.')
    print()
    wait_for_up_button_press()

    print()
    print('The test succeeded if  *** NOTHING happened ***')
    print('  ***  UNTIL your friend PRESSED the ** UP ** button.  ***')
    print()


def wait_for_up_button_press():
    """
    Constructs an ev3.Button object.
    Then repeatedly:
       1. Gets the STATE of the UP button on the ev3 BRICK
            and leaves the loop if that state is True
            (i.e., when the UP button is pressed).
       2. Sleeps for a small amount (say, 0.05 seconds).
    """
    # -------------------------------------------------------------------------
    # DONE: 4.  Implement and test this function.
    #           Tests have been written for you (above).
    # -------------------------------------------------------------------------
    button = ev3.Button()
    while True:
        if button.up == True:
            break
        else:
            time.sleep(.05)



def run_test_show_leds():
    """ Tests the   show_leds   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   show_leds   function:')
    print('--------------------------------------------------')

    print()
    print('Press the LEFT, RIGHT, UP, DOWN, and BACKSPACE buttons'
          + ' on the BRICK to change LED states.')
    print()
    show_leds()

def show_leds():
    """
    Constructs an ev3.Button object.
    Then, repeatedly make the LEDs behave as follows:
      If the user presses the:
       -- LEFT button:  The LEFT LED turns GREEN.
       -- RIGHT button: The RIGHT LED turns RED.
       -- UP button:    The LEFT LED turns AMBER.
       -- DOWN button:  Both LEDs turn off (i.e., to BLACK).
       -- BACKSPACE button: The program breaks out of the loop.
    """
    button = ev3.Button()
    while True:
        if button.backspace == True:
            break
        elif button.left == True:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)

        elif button.right == True:
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)

        elif button.up == True:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)

        elif button.down == True:
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.BLACK)
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)








# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

"""
Functions for SPINNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Zhihyu Wang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implment spin_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for spin_left_by_time.
#   Then repeat for spin_left_by_encoders.
#   Then repeat for the spin_right functions.


import ev3dev.ev3 as ev3
import time


def test_spin_left_spin_right():
    """
    Tests the spin_left and spin_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs spin_left_by_time.
      3. Same as #2, but runs spin_left_by_encoders.
      4. Same as #1, 2, 3, but tests the spin_right functions.
    """
    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    #test spin_left_seconds
    # while True:
    #     seconds = int(input('enter the seconds to travel :'))
    #     if seconds == 0:
    #         break
    #     else:
    #         speed = int(input('enter the speed to travel (-100 to 100) :'))
    #         stop_action = str(input('enter the Stop action ("brake", "coast" or "hold") :'))
    #         spin_left_seconds(seconds, speed, stop_action)

    # test spin_left_by_time
    # while True:
    #     degrees = int(input('enter the degree to travel :'))
    #     if degrees == 0:
    #         break
    #     else:
    #         speed = int(input('enter the speed to travel (-100 to 100) :'))
    #         stop_action = str(input('enter the Stop action ("brake", "coast" or "hold") :'))
    #         spin_left_by_time(degrees, speed, stop_action)

    # test spin_left_by_encoders
    # while True:
    #     degrees = int(input('enter the degree to travel :'))
    #     if degrees == 0:
    #         break
    #     else:
    #         speed = int(input('enter the speed to travel (-100 to 100) :'))
    #         stop_action = str(input('enter the Stop action ("brake", "coast" or "hold") :'))
    #         spin_left_by_encoders(degrees, speed, stop_action)

    #test spin_right_seconds
    #  while True:
    #     seconds = int(input('enter the seconds to travel :'))
    #     if seconds == 0:
    #         break
    #     else:
    #         speed = int(input('enter the speed to travel (-100 to 100) :'))
    #         stop_action = str(input('enter the Stop action ("brake", "coast" or "hold") :'))
    #         spin_right_seconds(seconds, speed, stop_action)

    # test spin_right_by_time
    # while True:
    #     degrees = int(input('enter the degree to travel :'))
    #     if degrees == 0:
    #         break
    #     else:
    #         speed = int(input('enter the speed to travel (-100 to 100) :'))
    #         stop_action = str(input('enter the Stop action ("brake", "coast" or "hold") :'))
    #         spin_right_by_time(degrees, speed, stop_action)

    # test spin_right_by_encoders
    # while True:
    #     degrees = int(input('enter the degree to travel :'))
    #     if degrees == 0:
    #         break
    #     else:
    #         speed = int(input('enter the speed to travel (-100 to 100) :'))
    #         stop_action = str(input('enter the Stop action ("brake", "coast" or "hold") :'))
    #         spin_right_by_encoders(degrees, speed, stop_action)


def spin_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot spin in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the given stop_action.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=-speed)
    right_motor.run_forever(speed_sp=speed)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)


def spin_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=-speed)
    right_motor.run_forever(speed_sp=speed)
    time.sleep(4*degrees/speed)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)



def spin_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """

    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_to_rel_pos(position_sp=-4.7*degrees, speed_sp=speed)
    right_motor.run_to_rel_pos(position_sp=4.7*degrees, speed_sp=speed)
    left_motor.wait_while(ev3.Motor.STATE_RUNNING)
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)



def spin_right_seconds(seconds, speed, stop_action):
    """ Calls spin_left_seconds with negative speeds to achieve spin_right motion. """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=speed)
    right_motor.run_forever(speed_sp=-speed)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)

def spin_right_by_time(degrees, speed, stop_action):
    """ Calls spin_left_by_time with negative speeds to achieve spin_right motion. """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=speed)
    right_motor.run_forever(speed_sp=-speed)
    time.sleep(4*degrees/speed)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)


def spin_right_by_encoders(degrees, speed, stop_action):
    """ Calls spin_left_by_encoders with negative speeds to achieve spin_right motion. """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_to_rel_pos(position_sp=4.7*degrees, speed_sp=speed)
    right_motor.run_to_rel_pos(position_sp=-4.7*degrees, speed_sp=speed)
    left_motor.wait_while(ev3.Motor.STATE_RUNNING)
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)
    left_motor.stop()
    right_motor.stop(stop_action=stop_action)

test_spin_left_spin_right()
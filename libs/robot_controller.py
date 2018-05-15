"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert self.left_motor.connected
        assert self.right_motor.connected
        self.running = True

    def forward(self, inches, speed, stop_action='brake'):
        degrees_motor = 88 * inches
        self.left_motor.run_to_rel_pos(position_sp=degrees_motor,
                                       speed_sp=speed,
                                       stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees_motor,
                                        speed_sp=speed,
                                        stop_action=stop_action)

        self.left_motor.wait_while('running')
        self.right_motor.wait_while('running')

    def go_forward(self, left_speed, right_speed):
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        assert left_motor.connected
        left_motor.run_forever(speed_sp=left_speed)
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert right_motor.connected
        right_motor.run_forever(speed_sp=right_speed)

    def turn_left(self, right_speed):
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert right_motor.connected
        right_motor.run_forever(speed_sp=right_speed)

    def turn_right(self, left_speed):
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        assert left_motor.connected
        left_motor.run_forever(speed_sp=left_speed)

    def stop(self):
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        assert left_motor.connected
        left_motor.stop()
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert right_motor.connected
        right_motor.stop()

    def go_backward(self, left_speed, right_speed):
        left_speed_b = - left_speed
        right_speed_b = - right_speed
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        assert left_motor.connected
        left_motor.run_forever(speed_sp=left_speed_b)
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert right_motor.connected
        right_motor.run_forever(speed_sp=right_speed_b)

    def arm_up(self):
        arm_motor = ev3.LargeMotor(ev3.OUTPUT_A)
        assert arm_motor.connected
        arm_motor.run_forever(speed_sp=50)
        touch_sensor = ev3.TouchSensor()
        while touch_sensor:
            arm_motor.stop()

    def arm_down(self):
        arm_motor = ev3.LargeMotor(ev3.OUTPUT_A)
        assert arm_motor.connected
        arm_motor.run_forever(speed_sp=-50)
        time.wait = 5
        arm_motor.stop()

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.1)

    def shutdown(self):
        self.running = False
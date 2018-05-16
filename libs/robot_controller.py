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
        self.running = True
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        assert self.left_motor.connected
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert self.right_motor.connected
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        assert self.arm_motor.connected
        self.touch_sensor = ev3.TouchSensor()
        assert self.touch_sensor.connected
        self.ir_sensor = ev3.InfraredSensor()
        assert self.ir_sensor.connected

    def go_forward(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def turn_left(self, right_speed):
        self.right_motor.run_forever(speed_sp=right_speed)

    def turn_right(self, left_speed):
        self.left_motor.run_forever(speed_sp=left_speed)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def go_backward(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=-left_speed)
        self.right_motor.run_forever(speed_sp=-right_speed)

    def arm_up(self):
        speed = 900
        self.arm_motor.run_forever(speed_sp=speed)
        while True:
            if self.touch_sensor.is_pressed:
                self.arm_motor.stop(stop_action='hold')
                ev3.Sound.speak("in position").wait()
                break

    def arm_down(self):
        speed = -900
        pos = -13000
        self.arm_motor.run_to_rel_pos(position=pos, speed_sp=speed)

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.01)

    def shutdown(self):
        self.running = False
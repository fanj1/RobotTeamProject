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
        self.color_sensor = ev3.ColorSensor()
        assert self.color_sensor
        self.line = False

    def go_forward(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def turn_left(self, left_speed, right_speed):
        self.right_motor.run_forever(speed_sp=right_speed)
        self.left_motor.run_forever(speed_sp=-int(left_speed))

    def turn_right(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=-int(right_speed))

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
        self.stop()

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

    def follow_black_line(self, white_level, black_level, speed):
        speed = int(speed)
        self.line = False
        while True:
            intensity = self.color_sensor.ambient_light_intensity
            if intensity >= white_level:
                self.stop()
                self.turn_left(speed / 2, speed)
                time.sleep(0.3)
            elif intensity <= black_level:
                self.go_forward(speed, speed)
            if self.line:
                break

    def follow_white_line(self, white_level, black_level, speed):
        speed = int(speed)
        while True:
            intensity = self.color_sensor.ambient_light_intensity
            if intensity <= black_level:
                self.stop()
                self.turn_left(speed / 2, speed)
                time.sleep(0.3)
            elif intensity >= white_level:
                self.go_forward(speed, speed)

    def seek_beacon(self):
        beacon_seeker = ev3.BeaconSeeker(channel=1)
        forward_speed = 300
        turn_speed = 100

        while not self.touch_sensor.is_pressed:
            current_heading = beacon_seeker.heading  # use the beacon_seeker heading
            current_distance = beacon_seeker.distance  # use the beacon_seeker distance
            if current_distance == -128:
                print("IR Remote not found. Distance is -128")
                self.stop()
            else:
                # If the absolute value of the current_heading is less than 2, you are on the right heading.
                #     If the current_distance is 0 return from this function, you have found the beacon!  return True
                #     If the current_distance is greater than 0 drive straight forward (forward_speed, forward_speed)
                # If the absolute value of the current_heading is NOT less than 2 but IS less than 10, you need to spin
                #     If the current_heading is less than 0 turn left (-turn_speed, turn_speed)
                #     If the current_heading is greater than 0 turn right  (turn_speed, -turn_speed)
                # If the absolute value of current_heading is greater than 10, then stop and print Heading too far off

                absolute_value_of_heading = math.fabs(current_heading)
                if absolute_value_of_heading < 2:
                    print("On the right heading. Distance: ", current_distance)
                    if current_distance <= 1:
                        self.go_forward(forward_speed, forward_speed)
                        time.sleep(1)
                        self.stop()
                        return True

                    if current_distance > 1:
                        self.go_forward(forward_speed, forward_speed)
                if absolute_value_of_heading > 2 and absolute_value_of_heading < 10:
                    print("Adjusting heading: ", current_heading)
                    if current_heading < 0:
                        self.turn_left(turn_speed, turn_speed)
                    if current_heading > 0:
                        self.turn_right(turn_speed, turn_speed)
                if absolute_value_of_heading > 10:
                    print("Heading is too far off to fix: ", current_heading)
                    self.stop()

            time.sleep(0.2)

        # The touch_sensor was pressed to abort the attempt if this code runs.
        print("Abandon ship!")
        self.stop()
        return False
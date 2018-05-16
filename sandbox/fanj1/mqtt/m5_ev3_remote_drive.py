#!/usr/bin/env python3
"""
For the full problem statement and details see the corresponding m5_pc_remote_drive.py comments.

There are many solutions to this problem.  The easiest solution on the EV3 side is to NOT bother makes a wrapper
class for the robot object.  Since the challenge presented is very direct it's easiest to just use the Snatch3r class
directly as the delegate to the MQTT client.

The code below is all correct.  The loop_forever line will cause a crash right now.  You need to implement that function
in the Snatch3r class in the library (remember the advice from the lecture).  Pick one team member to implement it then
have everyone else Git update.  Here is some advice for the Snatch3r method loop_forever and it's partner, shutdown.

    def loop_forever(self):
        # This is a convenience method that I don't really recommend for most programs other than m5.
        #   This method is only useful if the only input to the robot is coming via mqtt.
        #   MQTT messages will still call methods, but no other input or output happens.
        # This method is given here since the concept might be confusing.
        self.running = True
        while self.running:
            time.sleep(0.1)  # Do nothing (except receive MQTT messages) until an MQTT message calls shutdown.

    def shutdown(self):
        # Modify a variable that will allow the loop_forever method to end. Additionally stop motors and set LEDs green.
        # The most important part of this method is given here, but you should add a bit more to stop motors, etc.
        self.running = False

Additionally you will discover a need to create methods in your Snatch3r class to support drive, shutdown, stop, and
more. Once the EV3 code is ready, run it on the EV3 you can work on the PC side code for the MQTT Remote Control.

Author: David Fisher.
"""
import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3
import time


class Snatch3r(object):

    def __init__(self):
        self.running = True
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        assert self.left_motor.connected
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert self.right_motor.connected
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        assert self.arm_motor.connected
        self.touch = ev3.TouchSensor()

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
            if self.touch.is_pressed:
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


def main():
    print("--------------------------------------------")
    print(" Motion communication")
    print(" Press Back to exit when done.")
    print("--------------------------------------------")
    ev3.Sound.speak("Let's go").wait()

    robot = Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    # mqtt_client.connect_to_pc("35.194.247.175")  # Off campus IP address of a GCP broker

    robot.loop_forever()  # Calls a function that has a while True: loop within it to avoid letting the program end.


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------

main()

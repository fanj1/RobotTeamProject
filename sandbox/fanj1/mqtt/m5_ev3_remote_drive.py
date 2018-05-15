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
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        assert left_motor.connected
        left_motor.run_forever(speed_sp=-left_speed)
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert right_motor.connected
        right_motor.run_forever(speed_sp=-right_speed)

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

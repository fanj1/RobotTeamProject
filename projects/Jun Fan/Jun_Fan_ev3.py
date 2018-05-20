"""
This is the final project of CSSE120, 2018 Spring

Author: Jun Fan
"""

import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3
import time


class Delegate(object):

    def __init__(self):
        self.count = 0
        self.running = True
        self.run = True
        self.robot = robo.Snatch3r()

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.01)

    def start(self, speed, number):
        speed = int(speed)
        distance = self.robot.ir_sensor.proximity
        self.run = True
        while not self.run:
            if distance > 5:
                self.robot.follow_white_line(3, 1, 200)
            if distance < 5:
                self.robot.arm_up()
                self.robot.turn_right(speed, speed)
                time.sleep(2)
                self.robot.go_forward(speed, speed)
                time.sleep(1)
                self.robot.stop()
                self.robot.arm_down()
                self.robot.go_backward(speed, speed)
                time.sleep(1)
                self.robot.turn_left(speed, speed)
                time.sleep(2)
                self.robot.stop()
                self.count = self.count + 1
                if self.count == number:
                    self.robot.stop()
                    ev3.Sound.speak("picked up all rubbish").wait()
                    break
                ev3.Sound.speak("picked up one rubbish").wait()

    def stop(self):
        self.run = False

    def shutdown(self):
        self.running = False


def main():
    print("--------------------------------------------")
    print(" Motion communication")
    print(" Press Back to exit when done.")
    print("--------------------------------------------")
    ev3.Sound.speak("Let's go").wait()

    robot = Delegate()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()

    robot.loop_forever()


main()

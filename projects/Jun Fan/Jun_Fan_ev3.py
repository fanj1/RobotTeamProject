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
        self.distance = self.robot.ir_sensor.proximity

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.01)

    def start(self, speed, number):
        ev3.Sound.speak("start cleaning").wait()
        speed = int(speed)
        self.run = True
        while self.run:
            ev3.Sound.speak("hello").wait()
            if self.distance > 10:
                white_level = 3
                black_level = 1
                intensity = self.robot.color_sensor.ambient_light_intensity
                if intensity >= white_level:
                    self.stop()
                    self.robot.turn_left(speed / 2, speed)
                    time.sleep(0.3)
                elif intensity <= black_level:
                    self.robot.go_forward(speed, speed)
                    time.sleep(0.3)
            if self.distance < 10:
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
                ev3.Sound.speak("picked up one rubbish").wait()
                self.count = self.count + 1
                if self.count == number:
                    self.robot.stop()
                    ev3.Sound.speak("picked up all rubbish").wait()
                    break
        self.robot.stop()
        ev3.Sound.speak("stop").wait()

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

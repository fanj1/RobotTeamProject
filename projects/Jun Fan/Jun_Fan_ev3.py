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
            time.sleep(0.1)

    def start(self, speed, number):
        ev3.Sound.speak("start cleaning").wait()
        speed = int(speed)
        number = int(number)
        self.run = True
        self.count = 0
        while self.run:
            distance = self.robot.ir_sensor.proximity
            if distance > 4:
                white_level = 2
                black_level = 1
                intensity = self.robot.color_sensor.ambient_light_intensity
                if intensity >= white_level:
                    self.robot.go_forward(speed, speed)
                if intensity <= black_level:
                    self.robot.turn_left(speed / 2, speed)
            if distance < 4:
                self.robot.stop()
                self.robot.arm_up()
                self.robot.turn_right(speed, speed)
                time.sleep(300/speed)
                self.robot.go_forward(speed, speed)
                time.sleep(300/speed)
                self.robot.stop()
                self.robot.arm_down()
                time.sleep(5)
                self.robot.go_backward(speed, speed)
                time.sleep(300/speed)
                self.robot.turn_left(speed, speed)
                time.sleep(250/speed)
                self.robot.stop()
                ev3.Sound.speak("picked up one rubbish").wait()
                print('pick up one rubbish')
                self.count = self.count + 1
            if self.count == number:
                self.robot.stop()
                self.run = False
        self.robot.stop()
        time.sleep(2)
        ev3.Sound.speak("finish cleaning").wait()

    def stop(self):
        print('stop')
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

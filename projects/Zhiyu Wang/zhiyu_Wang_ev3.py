import ev3dev.ev3 as ev3
import math
import time
import mqtt_remote_method_calls as com
import traceback


class Snatch3r(object):
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
        self.number = True

    def go_forward(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def turn_left(self, left_speed, right_speed):
        self.right_motor.run_forever(speed_sp=right_speed)
        self.left_motor.run_forever(speed_sp=-int(left_speed))


    def turn_back_from_left(self,left_speed, right_speed):
        pos = 6000
        self.right_motor.run_to_rel_pos(position_sp=pos, speed_sp=right_speed)
        self.left_motor.run_to_rel_pos(position_sp=-pos, speed_sp=-int(left_speed))

    def turn_right(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=-int(right_speed))

    def turn_back_from_right(self, left_speed, right_speed):
        pos = 7000
        self.right_motor.run_to_rel_pos(position_sp=-pos, speed_sp=-int(right_speed))
        self.left_motor.run_to_rel_pos(position_sp=pos, speed_sp=left_speed)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        self.arm_motor.stop()

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
        pos = -5112
        self.arm_motor.run_to_rel_pos(position_sp=pos, speed_sp=speed)



    def follow_black_line(self, white_level, black_level, speed):
        speed = int(speed)
        while True:
            intensity = self.color_sensor.ambient_light_intensity
            if self.seek_beacon()== True:
                break
            if intensity >= white_level:
                self.turn_left(speed / 2, speed)
            elif intensity <= black_level:
                self.go_forward(speed, speed)
            if self.running==False:
                break

    def follow_white_line(self, white_level, black_level, speed):
        speed = int(speed)
        while True:
            intensity = self.color_sensor.ambient_light_intensity
            if self.seek_beacon()== True:
                break
            if intensity <= black_level:
                self.go_forward(speed / 2, speed)
            elif intensity >= white_level:
                self.go_forward(speed, speed)
            if self.running==False:
                break

    def seek_beacon(self):
        beacon_seeker = ev3.BeaconSeeker(channel=1)
        forward_speed = 200
        turn_speed = 100

        while not self.touch_sensor.is_pressed:
            current_heading = beacon_seeker.heading
            current_distance = beacon_seeker.distance
            if current_distance == -128:
                print("IR Remote not found. Distance is -128")
                return False
            else:
                absolute_value_of_heading = math.fabs(current_heading)
                if absolute_value_of_heading < 1:
                    print("On the right heading. Distance: ", current_distance)
                    if current_distance <= 1:
                        self.go_forward(100,100)
                        time.sleep(1.3)
                        self.stop()
                        return True

                    if current_distance > 1:
                        self.go_forward(forward_speed, forward_speed)
                if absolute_value_of_heading > 1 and absolute_value_of_heading < 5:
                    print("Adjusting heading: ", current_heading)
                    if current_heading < 0:
                        self.turn_left(turn_speed, turn_speed)
                    if current_heading > 0:
                        self.turn_right(turn_speed, turn_speed)
                if absolute_value_of_heading > 5:
                    print("Find nothing")
                    return False


    # def start_running(self, speed, white_value, black_value):
    #     while True:
    #         if self.out_loop == False:
    #             self.follow_white_line(speed, white_value, black_value)
    #         else:
    #             self.out_loop =True
    #             break


    def searching_mode(self, speed, white_value, black_value):
        try:
            while True:
                found_beacon = self.seek_beacon()
                print(found_beacon)
                if found_beacon:
                    ev3.Sound.speak("I find it")
                    self.arm_up()
                    self.turn_back_from_right(speed,speed)
                    time.sleep(3)
                    self.go_forward(speed,speed)
                    time.sleep(2)
                    self.stop()
                    self.arm_down()
                    time.sleep(6.5)
                    ev3.Sound.speak("trash removed")
                    self.go_backward(speed,speed)
                    time.sleep(2)
                    self.turn_back_from_left(speed,speed)
                    time.sleep(3)
                    break
                else:
                    self.follow_white_line(white_value, black_value,speed)


            self.stop()

        except:
            traceback.print_exc()
            ev3.Sound.speak("Error")

        print("Mission Complete!")
        ev3.Sound.speak("Mission Complete!").wait()

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.01)

    def shutdown(self):
        self.running = False

def main():
    print("--------------------------------------------")
    print(" CSSE120 Individual Project")
    print("--------------------------------------------")
    ev3.Sound.speak("I'm ready").wait()

    robot = Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()

    robot.loop_forever()

main()
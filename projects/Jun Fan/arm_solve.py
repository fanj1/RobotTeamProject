
import robot_controller as robo
import time
import ev3dev.ev3 as ev3


def main():
    # beacon_seeker = ev3.BeaconSeeker(channel=1)
    ir_sensor = ev3.InfraredSensor()
    assert ir_sensor.connected
    robot = robo.Snatch3r()
    # dis = beacon_seeker.distance
    ev3.Sound.speak("picked up all rubbish").wait()

    a = 0
    while True:
        distance = ir_sensor.proximity
        print(distance)
        # print(dis)
        if distance < 15:
            speed = 900
            robot.arm_motor.run_forever(speed_sp=speed)
            while True:
                if robot.touch_sensor.is_pressed:
                    robot.arm_motor.stop(stop_action='hold')
                    ev3.Sound.speak("in position").wait()
                    break
            robot.arm_motor.run_to_rel_pos(position_sp=-5112, speed_sp=-800)
            time.sleep(10)
            ev3.Sound.speak("done").wait()
        time.sleep(1)
        a = a + 1
        if a == 20:
            break


main()

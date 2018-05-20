
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
            robot.arm_up()
            robot.arm_down()
            robot.stop()
            break
        time.sleep(1)
        a = a + 1
        if a == 20:
            break


main()

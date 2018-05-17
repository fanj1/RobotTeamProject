
import robot_controller as robo
import time


def main():
    robot = robo.Snatch3r()
    robot.arm_up()
    time.sleep(1)
    robot.arm_down()


main()

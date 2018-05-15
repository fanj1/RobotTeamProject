

import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3
import time


def abc():
    arm_motor = ev3.LargeMotor(ev3.OUTPUT_A)
    assert arm_motor.connected
    arm_motor.run_forever(speed_sp=50)
    time.wait = 5
    arm_motor.stop(stopaction='hold')


abc()
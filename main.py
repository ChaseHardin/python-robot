from ev3dev.ev3 import *

Sound.beep().wait()


def drive_forward():
    print('start motors...')
    a_motor = LargeMotor('outA')
    b_motor = LargeMotor('outB')

    a_motor.run_timed(time_sp=3000, speed_sp=-750)
    b_motor.run_timed(time_sp=3000, speed_sp=-750)
    print('stop robot...')

drive_forward()

# m = LargeMotor('outB')
# m.run_timed(time_sp=3000, speed_sp=-750)
# print("set speed (speed_sp) = " + str(m.speed_sp))
# sleep(1)
# print("actual speed = " + str(m.speed))
# sleep(4)

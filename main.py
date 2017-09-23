from time import sleep

from ev3dev.ev3 import *

a_motor = LargeMotor('outA')
b_motor = LargeMotor('outB')


def message(speak):
    Sound.speak(speak).wait()


def drive_forward():
    a_motor.run_timed(time_sp=6000, speed_sp=-750)
    b_motor.run_timed(time_sp=6000, speed_sp=-750)


def drive_backwards():
    a_motor.run_timed(time_sp=6000, speed_sp=750)
    b_motor.run_timed(time_sp=6000, speed_sp=750)


Sound.speak('Hello, Chase').wait()
sleep(2)

drive_forward()

sleep(2)
Sound.speak('I am done...').wait()
sleep(2)

drive_backwards()

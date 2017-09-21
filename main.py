from time import sleep

from ev3dev.ev3 import *

a_motor = LargeMotor('outA')
b_motor = LargeMotor('outB')

Sound.beep().wait()


def message(speak):
    Sound.speak(speak).wait()


def drive_forward():
    a_motor.run_timed(time_sp=3000, speed_sp=-750)
    b_motor.run_timed(time_sp=3000, speed_sp=-750)


def drive_backwards():
    a_motor.run_timed(time_sp=3000, speed_sp=750)
    b_motor.run_timed(time_sp=3000, speed_sp=750)

message('Starting my motors!')
sleep(4)
drive_forward()

sleep(4)
message('Reversing directions!')
drive_backwards()

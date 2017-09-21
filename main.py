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


message('Starting the motors... please keep your hands inside of the vehicle')
sleep(2)

drive_forward()
sleep(2)
message('Driving backwards')
drive_backwards()
sleep(2)
message('Thanks for riding the mindstorm robot.')

# message('Reversing directions!').wait()
# drive_backwards()

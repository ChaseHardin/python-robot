from ev3dev.ev3 import *

from src.drive.drive_command import Drive

a_motor = LargeMotor('outA')
b_motor = LargeMotor('outB')


def message(speak):
    Sound.speak(speak).wait()


drive_command = Drive()

drive_command.forward()
drive_command.backwards()
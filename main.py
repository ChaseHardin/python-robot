from time import sleep

from src.drive.drive_command import DriveCommand

drive_command = DriveCommand()

drive_command.forward()
sleep(2)
drive_command.backwards()

from ev3dev.core import Sound

from src.drive.drive_command import DriveCommand

drive_command = DriveCommand()

Sound.tone([(3000, 2000, 400), (800, 1800, 2000)]).wait()

drive_command.move(time_sp=5000, speed_sp=-750)
drive_command.move(time_sp=5000, speed_sp=750)

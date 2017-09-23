from src.drive.drive_command import DriveCommand

drive_command = DriveCommand()

drive_command.move(time_sp=5000, speed_sp=-750)
drive_command.move(time_sp=5000, speed_sp=750)

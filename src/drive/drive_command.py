
from ev3dev.core import LargeMotor


class DriveCommand:
    a_motor = LargeMotor('outA')
    b_motor = LargeMotor('outB')

    def move(self, time_sp, speed_sp):
        self.a_motor.run_timed(time_sp=time_sp, speed_sp=speed_sp)
        self.b_motor.run_timed(time_sp=time_sp, speed_sp=speed_sp)

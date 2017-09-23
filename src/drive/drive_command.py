from ev3dev.core import LargeMotor


class Drive:
    a_motor = LargeMotor('outA')
    b_motor = LargeMotor('outB')

    def forward(self):
        self.a_motor.run_timed(time_sp=6000, speed_sp=-750)
        self.b_motor.run_timed(time_sp=6000, speed_sp=-750)

    def backwards(self):
        self.a_motor.run_timed(time_sp=6000, speed_sp=750)
        self.b_motor.run_timed(time_sp=6000, speed_sp=750)

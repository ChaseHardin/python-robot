from ev3dev.core import LargeMotor, Sound

a_motor = LargeMotor('outA')
b_motor = LargeMotor('outB')


def move(time_sp, speed_sp):
    a_motor.run_timed(time_sp=time_sp, speed_sp=speed_sp)
    b_motor.run_timed(time_sp=time_sp, speed_sp=speed_sp)


Sound.speak('Starting my motors...')

a_motor.wait_while('speaking')
b_motor.wait_while('speaking')

move(time_sp=5000, speed_sp=-750)
a_motor.wait_while('running')
b_motor.wait_while('running')


move(time_sp=5000, speed_sp=750)

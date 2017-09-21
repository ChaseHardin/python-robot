from ev3dev.ev3 import *
from time import sleep

Sound.beep().wait()

m = LargeMotor('outB')
m.run_timed(time_sp=3000, speed_sp=-750)
print("set speed (speed_sp) = " + str(m.speed_sp))
sleep(1)
print("actual speed = " + str(m.speed))
sleep(4)

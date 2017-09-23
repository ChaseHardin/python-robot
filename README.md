# Python-Robot

This is my repo dedicated to learning the Lego Mindstorm EV3 Robot. This robot was setup by following [EV3 Dev's documentation.](http://www.ev3dev.org/)

# Example Code Snippets

### Make Sound, Then Run Motors

```
from ev3dev.core import LargeMotor

a_motor = LargeMotor('outA')
b_motor = LargeMotor('outB')

def move(time_sp, speed_sp):
    a_motor.run_timed(time_sp=time_sp, speed_sp=speed_sp)
    b_motor.run_timed(time_sp=time_sp, speed_sp=speed_sp)
    a_motor.wait_while('running')
    b_motor.wait_while('running')
    
# run code
Sound.tone([(3000, 2000, 400), (800, 1800, 2000)]).wait() 

move(time_sp=5000, speed_sp=-750)
move(time_sp=5000, speed_sp=750)
```
from ev3dev.core import Sound, InfraredSensor

Sound.tone(1500, 2000).wait()

ir = InfraredSensor()
assert ir.connected, "Connect a single infrared sensor to any sensor port"

# ir.mode = 'IR-PROX'

count = 0

while count < 100:
    print("Distance:: ", ir.value())
    count += 1

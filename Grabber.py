import force_sensor
from hub import port
import motor

def is_force_sensor_pressed():
    return force_sensor.pressed(port.E)
def is_force_sensor_not_pressed():
    return not force_sensor.pressed(port.E)

while True:
    if is_force_sensor_pressed():
        motor.run_for_degrees(port.F, -100, 100)
    elif is_force_sensor_not_pressed():
        motor.run_for_degrees(port.F, 100, 100)
        

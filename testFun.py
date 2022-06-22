import time

from SensorPackages.InfineonSensor import InfineonSensor

sensor = InfineonSensor()
sensor.setState('cont_temp')
print(sensor.getID())

print(sensor.getState())
print(sensor.current_scale_factor)
print(sensor.getCompensatedTemp())
import sys


# I2C channel 1 is connected to the GPIO pins
sys.path.insert(1, '/home/ivar/Repos/Sensor project/')
from SensorPackages.InfineonSensor import InfineonSensor

sensor = InfineonSensor()

t_raw = sensor.getTRaw()

print(t_raw)
print(int(t_raw, 2))

import sys


# I2C channel 1 is connected to the GPIO pins
sys.path.insert(1, '/home/ivar/Repos/Sensor project/')
import validation
import ByteTools
from SensorClass import InfineonSensor

sensor = InfineonSensor()

t_raw = sensor.getTRaw()

print(t_raw)

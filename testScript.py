#from SensorPackages.InfineonSensor import InfineonSensor
import ByteTools
'''
obj = InfineonSensor()
print(obj.getState())
meas_config_address = obj.getAddress('meas_config')

key = 'cont_temp'
obj.setState(key)
print(obj.getState())
actual = bin(obj.readAddress(meas_config_address))
print(actual)
actual = ByteTools.getBits(actual, [2, 1, 0])

print(obj.getState())

expected = ByteTools.to3Bit(obj.states[key])

print(actual)
print(expected)
'''

print(ByteTools.getBits(0b11100110, [2, 1, 0]))
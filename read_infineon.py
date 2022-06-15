import smbus2
import sys


# I2C channel 1 is connected to the GPIO pins
sys.path.insert(1, '/home/ivar/Repos/Sensor project/')
import validation
import ByteTools

channel = 1

address = 0x76
temp_address = [0x03, 0x04, 0x05]
press_address = [0x00, 0x01, 0x02]
ID_address = 0x0D
press_config = 0x06
temp_config = 0x07

# Initialize I2C (SMBus)
bus = smbus2.SMBus(channel)

# Init methods
# bus.write_byte_data(address, 0x08, 0x02)
bus.write_byte_data(address, 0x08, 0x06)
temp_coefficients = [0x10, 0x12]

for i in range(0, len(temp_coefficients)):
    byte = bus.read_byte_data(address, temp_coefficients[i])
    temp_coefficients[i] = ByteTools.bin2int([bin(byte)], 8)

print(temp_coefficients)

bits = ["", "", ""]
for i in range(0, 3):
    bit = bus.read_byte_data(address, temp_address[i])
    bits[i] = bit

raw_temp = ByteTools.combineBytes(bits, 8)
print(raw_temp)
raw_temp = int(raw_temp,2)
print(raw_temp)
scale_factor = 253952

temp_raw = raw_temp/scale_factor

print(temp_raw)

temp_comp = temp_coefficients[0]*0.5 + temp_coefficients[1]*temp_raw

print(temp_comp)
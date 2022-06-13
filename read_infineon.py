import smbus2

# I2C channel 1 is connected to the GPIO pins
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

bits = ["", "", ""]
for i in range(0, 3):
    bit = bus.read_byte_data(address, temp_address[i])
    bits[i] = bin(bit)

print(ByteTools.bin2int(bits, 8))

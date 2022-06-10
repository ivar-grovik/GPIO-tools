import smbus2

# I2C channel 1 is connected to the GPIO pins
channel = 1


address = 0x76
temp_address = [0x03, 0x04, 0x05]
press_address = [0x00, 0x01, 0x02]
ID_address = 0x0D
press_config = 0x06
temp_config = 0x07
meas_config = 0x08



# Initialize I2C (SMBus)
bus = smbus2.SMBus(channel)

# Create a sawtooth wave 16 times
cont = True



#Read temperature
for i in range(0, 3):
    print(temp_address[i])
    print(bus.read_i2c_block_data(address,temp_address[i]))

    print(bus.read_byte_data(address,temp_address[i]))
    print("\n")


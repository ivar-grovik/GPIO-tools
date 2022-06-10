
import smbus

# I2C channel 1 is connected to the GPIO pins
channel = 1

#  MCP4725 defaults to address 0x60
address = 0x76
temp_address = [0x03, 0x04, 0x05]
press_address = [0x00, 0x01, 0x02]
ID_address = 0x0D
press_config = 0x06
temp_config = 0x07
meas_config = 0x08

# Register addresses (with "normal mode" power-down bits)
reg_write_dac = 0x40

# Initialize I2C (SMBus)
bus = smbus.SMBus(channel)

# Create a sawtooth wave 16 times
cont = True



#Read temperature
for i in range(0, 3):
    print("hei")
    print(temp_address[i])
    print(bus.read_i2c_block_data(address,temp_address[i]))

    print(bus.read_byte_data(address,temp_address[i]))
    print("\n")


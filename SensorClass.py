from abc import ABC, abstractmethod
import smbus2
import ByteTools


class SensorClass(ABC):
    def __init__(self, identifier, addresses, scale_factors, bus):
        self.identifier = identifier
        self.addresses = addresses
        self.scale_factors = scale_factors
        self.bus = bus

    @property
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def initRead(self):
        pass

    def getAddress(self, address_type):
        return self.addresses[address_type]


class InfineonSensor(SensorClass):
    @property
    def read(self):
        print(self.identifier)

    def initRead(self):
        self.bus.write_byte_data(self.addresses["sm_address"], self.addresses["meas_config"], 0x06)

    def getTRaw(self):
        addresses = self.temp_address
        bits = ["", "", ""]
        for i in range(0, 3):
            bit = self.bus.read_byte_data(self.addresses["sm_address"], addresses[i])
            bits[i] = bin(bit)

        raw_temp = ByteTools.bin2int(bits, 8)

        return raw_temp

    def __init__(self):
        addresses = {
            "channel": 1,
            "sm_address": 0x76,
            "ID_address": 0x0D,
            "temp_address": [0x03, 0x04, 0x05],  # high, medium, low
            "press_address": [0x00, 0x01, 0x02],  # high, medium, low
            "meas_config": 0x08,
            "press_config": 0x06,
            "temp_config": 0x07,
            "temp_coefficients": [0x10, 0x12]  # c0, c1
        }
        scale_factors = {
            1: 524288,
            2: 1572864,
            4: 3670016,
            8: 3670016,
            16: 253952,
            32: 516096,
            64: 1040384,
            128: 2088960
        }
        bus = smbus2.SMBus(addresses["channel"])
        super().__init__("Infineon", addresses, scale_factors, bus)

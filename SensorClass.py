from abc import ABC, abstractmethod
import sys

sys.path.insert(1, '/home/ivar/Repos/Sensor project/')
import smbus2
import ByteTools
import validation


class SensorClass(ABC):
    def __init__(self, identifier, addresses, states, scale_factors, bus):
        self.identifier = identifier
        self.addresses = addresses
        self.scale_factors = scale_factors
        self.bus = bus
        self.states = states

    @property
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def setState(self):
        pass

    def getAddress(self, address_type):
        return self.addresses[address_type]


class InfineonSensor(SensorClass):
    @property
    def read(self):
        print(self.identifier)

    def setState(self, state):
        validation.mustBeMember(state, self.states.keys())
        hex_state = self.states[state]
        self.bus.write_byte_data(self.addresses["sm_address"], self.addresses["meas_config"], hex_state)

    def getID(self):
        self.setState('cont_temp')
        sm_address = self.addresses["sm_address"]
        id_address = self.addresses["ID_address"]
        return hex(self.bus.read_byte_data(sm_address, id_address))

    def getTRaw(self):
        addresses = self.addresses["temp_address"]
        bits = ["", "", ""]
        for i in range(0, 3):
            bit = self.bus.read_byte_data(self.addresses["sm_address"], addresses[i])
            bits[i] = bit

        raw_temp = ByteTools.combineBytes(bits, 8)

        return raw_temp

    def getCoef(self, type_coef):
        validation.mustBeMember(type_coef, ["pressure", "temp"])
        if type_coef == "pressure":
            coef = self.addresses["press_coefficients"]
        elif type_coef == "temp":
            coef = self.addresses["temp_coefficients"]
        return coef

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
            "temp_coefficients": [0x10, 0x12],  # c0, c1
            "press_coefficients": [0x13, 0x16, 0x1c, 0x20, 0x18, 0x1a, 0x1e]  # c00, c10, c20, c30, c01, c11, c21
        }
        states = {
            "stand-by": 0x00,
            "press_meas": 0x01,
            "temp_meas": 0x02,
            "cont_press": 0x05,
            "cont_temp": 0x06,
            "cont_both": 0x07
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
        super().__init__("Infineon", addresses, states, scale_factors, bus)

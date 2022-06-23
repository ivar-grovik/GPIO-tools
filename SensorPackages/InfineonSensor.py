import time

from SensorPackages.SensorClass import SensorClassAbstract
import smbus2
import ByteTools
import validation
import string


class InfineonSensor(SensorClassAbstract):
    @property
    def read(self):
        print(self.identifier)

    def getID(self):
        sm_address = self.getAddress("sm_address")
        id_address = self.getAddress("ID_address")
        return hex(self.bus.read_byte_data(sm_address, id_address))

    def reset(self):
        reset_address = self.getAddress("reset")
        byte = 0b1001
        self.writeAddress(reset_address, byte)
        time.sleep(5)

    def getState(self):
        sm_address = self.getAddress("sm_address")
        config_address = self.addresses["meas_config"]
        state = bin(self.bus.read_byte_data(sm_address, config_address))

        state = ByteTools.getBits(state, [2, 1, 0])

        state = int(state, 2)
        all_states = self.states

        return list(all_states.keys())[list(all_states.values()).index(state)]

    def setState(self, state):
        validation.mustBeMember(state, self.states.keys())
        state = ByteTools.to3Bit(bin(self.states[state]))

        sm_address = self.getAddress("sm_address")
        config_address = self.addresses["meas_config"]
        old_value = bin(self.bus.read_byte_data(sm_address, config_address))

        bits = ByteTools.bin2List(state)

        old_value = ByteTools.changeBit(old_value, bits, [2, 1, 0])

        self.bus.write_byte_data(sm_address, config_address, int(old_value, 2))

    def writeAddress(self, address, byte):
        sm_address = self.getAddress('sm_address')
        self.bus.write_byte_data(sm_address, address, byte)

    def readAddress(self, addresses):

        sm_address = self.getAddress('sm_address')
        if isinstance(addresses, list):
            byte = []
            for address in addresses:
                byte.append(self.bus.read_byte_data(sm_address, address))
        else:
            byte = self.bus.read_byte_data(sm_address, addresses)
        return byte

    def getAddress(self, address_name):
        validation.mustBeMember(address_name, self.addresses.keys())
        return self.addresses[address_name]

    def setTempSampling(self, num_samples):
        validation.mustBeMember(num_samples, self.scale_factors.keys())

        self.current_scale_factor = self.scale_factors[num_samples]

    def setTempConfig(self, sensor, meas_rate, precision):
        sensor_config = {
            "internal": 0,
            "external": 1
        }

        validation.mustBeMember(sensor, sensor_config.keys())
        validation.mustBeMember(meas_rate, self.meas_rates.keys())
        validation.mustBeMember(precision, self.precisions.keys())

        self.current_meas_rate = self.meas_rates[meas_rate]
        self.current_precision = self.precisions[precision]

        self.setTempSampling(precision)

    def getScaleFactor(self):
        return self.current_scale_factor

    def getCoef(self, type_coef):
        validation.mustBeMember(type_coef, ["pressure", "temp"])
        if type_coef == "pressure":
            coef = self.addresses["press_coefficients"]
        elif type_coef == "temp":
            coef = self.addresses["temp_coefficients"]
        return coef

    # Temperature
    def getTRaw(self):
        addresses = self.getAddress("temp_address")
        bits = self.readAddress(addresses)

        raw_temp = ByteTools.combineBytes(bits, 8)

        return raw_temp

    def getTempScaled(self):
        scale_factor = self.getScaleFactor()

        t_raw = int(self.getTRaw(), 2)

        temp_scaled = t_raw / scale_factor

        return temp_scaled

    def getCompensatedTemp(self):
        coeff_address = self.getAddress('temp_coefficients')
        coeffs = self.readAddress(coeff_address)

        temp_scaled = self.getTempScaled()

        return coeffs[0] * 0.5 + coeffs[1] * temp_scaled

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
            "press_coefficients": [0x13, 0x16, 0x1c, 0x20, 0x18, 0x1a, 0x1e],  # c00, c10, c20, c30, c01, c11, c21
            "reset": 0x0c
        }
        states = {
            "stand-by": 0b000,
            "press_meas": 0b001,
            "temp_meas": 0b010,
            "cont_press": 0b101,
            "cont_temp": 0b110,
            "cont_both": 0b111
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
        self.setState('stand-by')
        self.setTempSampling(1)
        self.meas_rates = {
            "1": 0b000,
            "2": 0b001,
            "4": 0b010,
            "8": 0b011,
            "16": 0b100,
            "32": 0b101,
            "64": 0b110,
            "128": 0b111
        }
        self.precisions = {
            "1": 0b0000,
            "2": 0b0001,
            "4": 0b0010,
            "8": 0b0011,
            "16": 0b100,
            "32": 0b0101,
            "64": 0b110,
            "128": 0b0111
        }

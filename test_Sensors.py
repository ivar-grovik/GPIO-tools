import time
import unittest
import ByteTools
from SensorPackages.SensorFactory import createObj


class InfineonTests(unittest.TestCase):
    def setUp(self):
        self.obj = createObj("Infineon")


    def test_ReadID(self):
        id = self.obj.getID()
        self.assertEqual(id, hex(0x10))

    def test_reset(self):
        meas_config_address = self.obj.getAddress('meas_config')
        self.obj.setState("temp_meas")

        key = 'stand-by'

        self.obj.reset()

        actual = bin(self.obj.readAddress(meas_config_address))
        actual = ByteTools.getBits(actual, [2, 1, 0])

        expected = ByteTools.to3Bit(self.obj.states[key])

        self.assertEqual(actual, expected)

    def test_stand_by(self):
        meas_config_address = self.obj.getAddress('meas_config')
        #test standby

        key = 'stand-by'
        self.obj.setState(key)

        actual = bin(self.obj.readAddress(meas_config_address))
        actual = ByteTools.getBits(actual, [2, 1, 0])

        expected = ByteTools.to3Bit(self.obj.states[key])

        self.assertEqual(actual, expected)
    
    def test_temp_meas(self):
        #test temp measurement
        meas_config_address = self.obj.getAddress('meas_config')

        key = 'temp_meas'
        self.obj.setState(key)
        print(self.obj.getState())
        actual = bin(self.obj.readAddress(meas_config_address))
        actual = ByteTools.getBits(actual, [2, 1, 0])

        expected = ByteTools.to3Bit(self.obj.states[key])

        self.assertEqual(actual, expected)

    def test_press_meas(self):
        # test temp measurement
        meas_config_address = self.obj.getAddress('meas_config')

        key = "press_meas"
        self.obj.setState(key)
        actual = bin(self.obj.readAddress(meas_config_address))
        actual = ByteTools.getBits(actual, [2, 1, 0])

        expected = ByteTools.to3Bit(self.obj.states[key])
        self.assertEqual(actual, expected)

    def test_press_cont(self):
        # test press measurement
        print(self.obj.getState())
        meas_config_address = self.obj.getAddress('meas_config')

        key = 'cont_press'
        self.obj.setState(key)
        actual = bin(self.obj.readAddress(meas_config_address))
        actual = ByteTools.getBits(actual, [2, 1, 0])

        print(self.obj.getState())

        expected = ByteTools.to3Bit(self.obj.states[key])

        self.assertEqual(actual, expected)

    def test_temp_cont(self):
        # test temp measurement
        meas_config_address = self.obj.getAddress('meas_config')

        key = 'cont_temp'
        self.obj.setState(key)
        actual = bin(self.obj.readAddress(meas_config_address))
        actual = ByteTools.getBits(actual, [2, 1, 0])

        expected = ByteTools.to3Bit(self.obj.states[key])
        self.assertEqual(actual, expected)
    
    def test_both_cont(self):
        # test temp measurement
        meas_config_address = self.obj.getAddress('meas_config')

        key = 'cont_both'
        self.obj.setState(key)
        actual = bin(self.obj.readAddress(meas_config_address))
        actual = ByteTools.getBits(actual, [2, 1, 0])

        expected = ByteTools.to3Bit(self.obj.states[key])
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

InfineonTests.test_temp_meas()
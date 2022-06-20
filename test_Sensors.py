import unittest
import ByteTools
from SensorPackages.SensorFactory import createObj


class InfineonTests(unittest.TestCase):
    def setUp(self):
        self.obj = createObj("Infineon")


    def test_ReadID(self):
        id = self.obj.getID()
        self.assertEqual(id, hex(0x10))

    def test_intConvertion(self):
        expected = 5
        actual = ByteTools.str2int('0b101')

        self.assertEqual(actual, expected)

        actual = ByteTools.str2int('0x05')

        self.assertEqual(actual, expected)

    def test_listConvertion(self):
        expected = [1, 5, 11]
        actual = ByteTools.str2int(['0b1', '0b101', '0b1011'])

        self.assertEqual(actual, expected)

        actual = ByteTools.str2int(['0x01', '0x05', '0x0b'])

        self.assertEqual(actual, expected)
    # def test_initializes(self):
    # self.obj.init
    # self.obj.

    def test_stand_by(self):
        meas_config_address = self.obj.getAddress('meas_config')
        #test standby

        key = 'stand-by'
        self.obj.setState(key)

        actual = bin(self.obj.readAddress(meas_config_address))
        actual = int(actual[7:], 2)

        expected = self.obj.states[key]

        self.assertEqual(actual, expected)

    def test_temp_meas(self):
        #test temp measurement
        meas_config_address = self.obj.getAddress('meas_config')

        key = 'stand-by'
        self.obj.setState(key)

        key = 'temp_meas'
        self.obj.setState(key)

        actual = bin(self.obj.readAddress(meas_config_address))

        expected = self.obj.states[key]
        actual = int(actual[7:], 2)
        self.assertEqual(actual, expected)

    def test_press_meas(self):
        # test temp measurement
        meas_config_address = self.obj.getAddress('meas_config')

        key = 'stand-by'
        self.obj.setState(key)

        key = "press_meas"
        self.obj.setState(key)
        actual = bin(self.obj.readAddress(meas_config_address))
        actual = int(actual[7:], 2)

        expected = self.obj.states[key]
        self.assertEqual(actual, expected)

    def test_press_cont(self):
        # test press measurement
        meas_config_address = self.obj.getAddress('meas_config')

        key = 'stand-by'
        self.obj.setState(key)

        key = 'cont_press'
        self.obj.setState(key)
        actual = bin(self.obj.readAddress(meas_config_address))

        actual = int(actual[7:], 2)
        expected = self.obj.states[key]

        self.assertEqual(actual, expected)

    def test_temp_cont(self):
        # test temp measurement
        meas_config_address = self.obj.getAddress('meas_config')

        key = 'stand-by'
        self.obj.setState(key)

        key = 'cont_temp'
        self.obj.setState(key)
        actual = bin(self.obj.readAddress(meas_config_address))
        actual = int(actual[7:], 2)

        expected = self.obj.states[key]
        self.assertEqual(actual, expected)

    def test_both_cont(self):
        # test temp measurement
        meas_config_address = self.obj.getAddress('meas_config')

        key = 'stand-by'
        self.obj.setState(key)

        key = 'cont_both'
        self.obj.setState(key)
        actual = bin(self.obj.readAddress(meas_config_address))
        actual = int(actual[7:], 2)

        expected = self.obj.states[key]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

InfineonTests()
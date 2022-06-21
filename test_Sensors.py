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
        actual = ByteTools.getBits(actual, [1, 2, 3])
        print(actual)
        expected = ByteTools.to3Bit(self.obj.states[key])

        self.assertEqual(actual, expected)
    '''
    def test_reset_2(self):
        meas_config_address = self.obj.getAddress('meas_config')
       % press_address = self.obj.getAddress("press_meas")
        self.obj.setState("temp_meas")

        key = 'stand-by'

        actual = bin(self.obj.readAddress(meas_config_address))
        actual = int(actual[7:], 2)

        expected = ByteTools.to3Bit(self.obj.states[key])

        self.assertEqual(actual, expected)
    
    def test_stand_by(self):
        meas_config_address = self.obj.getAddress('meas_config')
        #test standby

        key = 'stand-by'
        self.obj.setState(key)

        actual = bin(self.obj.readAddress(meas_config_address))
        print(actual)
        print(actual[7:])
        actual = int(actual[7:], 2)

        expected = ByteTools.to3Bit(self.obj.states[key])
        print(expected)
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
    '''
if __name__ == '__main__':
    unittest.main()

InfineonTests()
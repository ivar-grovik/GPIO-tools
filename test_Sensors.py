import unittest
import sys
sys.path.insert(1, '/home/ivar/Repos/Sensor project/')
import SensorClass
import ByteTools


class InfineonTests(unittest.TestCase):
    def setUp(self):
        self.obj = SensorClass.InfineonSensor()

    def test_ReadID(self):
        id = self.obj.getID()
        self.assertEqual(id, hex(0x10))  # add assertion here

    def test_intConvertion(self):
        expected = 5
        actual = ByteTools.str2int('0b101')

        self.assertEqual(actual, expected)

        actual = ByteTools.str2int('0x101')

        self.assertEqual(actual, expected)

    #def test_initializes(self):
        #self.obj.init
        #self.obj.
"""
    def test_ConvertBytes(self):
        expected = 0x10203
        value_array = [['0x03', '0x02', '0x01'], ['0b11', '0x10', '0x01'], [3, 2, 1]]
        for i in range(0, len(value_array)):
            values = value_array[i]
            print(values)
            print(values[0])
            print(type(values[0]))
            if type(values[0]) == 'str':
                values = ByteTools.str2int(value_array[i])
            print(values)
            print('hei')
            value = ByteTools.combineBytes(values, 8)

            value = int(value, 2)

            self.assertEqual(expected, value)
"""



if __name__ == '__main__':
    unittest.main()

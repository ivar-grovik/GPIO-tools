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

    #def test_initializes(self):
        #self.obj.init
        #self.obj.

    def test_ConvertBytes(self):
        expected = 0x10203
        value_array = [[0x03, 0x02, 0x01], ['0b11', '0x10', '0x01'], [3, 2, 1]]
        for i in range(0, len(value_array)):
            value = ByteTools.combineBytes(value_array[i], 8)

            value = int(value, 2)

            self.assertEqual(expected, value)




if __name__ == '__main__':
    unittest.main()

import unittest
import sys
sys.path.insert(1, '/home/ivar/Repos/Sensor project/')
import SensorClass


class InfineonTests(unittest.TestCase):
    def setUp(self):
        self.obj = SensorClass.InfineonSensor()

    def test_ReadID(self):
        id = self.obj.getID()
        print(id)
        self.assertEqual(id, hex(0x10))  # add assertion here

    #def test_initializes(self):
        #self.obj.init
        #self.obj.



if __name__ == '__main__':
    unittest.main()

InfineonTests.run()

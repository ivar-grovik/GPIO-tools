import unittest
import sys
sys.path.insert(1, '/home/ivar/Repos/Sensor project/')
import SensorClass


class InfineonTests(unittest.TestCase):
    def setUp(self):
        self.obj = SensorClass.InfineonSensor()

    def test_ReadID(self):
        id = self.obj.getID()
        self.assertEqual(id, 16)  # add assertion here




if __name__ == '__main__':
    unittest.main()

InfineonTests.run()

import unittest
import sys
sys.path.insert(1, '/home/ivar/Repos/Sensor project/')
import SensorClass


class InfineonTests(unittest.TestCase):
    def readID(self):
        id = self.obj.getID()
        self.assertEqual(id, 16)  # add assertion here

    def setUp(self):
        print("hei")
        self.obj = SensorClass.InfineonSensor()


if __name__ == '__main__':
    print("hei")
    unittest.main()

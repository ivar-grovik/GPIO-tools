import unittest

import SensorClass


class InfineonTests(unittest.TestCase):
    def readID(self):
        id = self.obj.getID()
        self.assertEqual(id, 16)  # add assertion here

    def setUp(self):
        self.obj = SensorClass.InfineonSensor()

if __name__ == '__main__':
    unittest.main()


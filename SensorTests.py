import unittest

import SensorClass


class InfineonTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setUp(self):
        self.obj = SensorClass.InfineonSensor()

if __name__ == '__main__':
    unittest.main()

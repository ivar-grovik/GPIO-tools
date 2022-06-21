import unittest
import ByteTools


class BitTests(unittest.TestCase):

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

    def test_changeBits(self):
        num = 0
        byte = ByteTools.to8Bit(num)



        actual = ByteTools.changeBit(byte, [1, 1, 1], [1, 5, 8])
        expected = "0b10010001"
        self.assertEqual(actual, expected)  # add assertion here

    def test_to8Bit(self):
        numbers = [0, 1, 5]
        expectations = ["0b00000000", "0b00000001", "0b00000101"]

        for i in range(0, len(numbers)):
            actual = ByteTools.to8Bit(numbers[i])
            expected = expectations[i]

            self.assertEqual(actual, expected)

    def test_bin2list(self):
        actuals = ["0b0101", "0b1101", "0b001000"]
        expectations = [[0, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 0, 0, 0]]

        for i in range(0, len(actuals)):
            actual = actuals[i]
            expected = expectations[i]

            actual = ByteTools.bin2List(actual)

            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

BitTests()
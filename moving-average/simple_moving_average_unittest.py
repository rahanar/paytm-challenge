import unittest

from simple_moving_average import SimpleMovingAverage

class TestSimpleMovingAverage(unittest.TestCase):

    def setUp(self):
        self.sma = SimpleMovingAverage(4)

    def test_empty_queue(self):
        self.assertEqual(self.sma.getMovingAverage(), 0.0)
        self.assertEqual(self.sma.getElements(), [])

    def test_add_element(self):
        self.sma.addElement(3)
        self.assertEqual(self.sma.getMovingAverage(), 0.75)
        self.assertEqual(self.sma.getElements(), [3])

    def test_add_multiple_elements(self):
        for i in range(3, 7, 1):
            self.sma.addElement(i)
        self.assertEqual(self.sma.getMovingAverage(), 4.5)
        self.assertEqual(self.sma.getElements(), [3, 4, 5, 6])

    def test_add_five_elements(self):
        for i in range(3, 7, 1):
            self.sma.addElement(i)
        self.assertEqual(self.sma.getMovingAverage(), 4.5)
        self.assertEqual(self.sma.getElements(), [3, 4, 5, 6])
        self.sma.addElement(7)
        self.assertEqual(self.sma.getMovingAverage(), 5.5)
        self.assertEqual(self.sma.getElements(), [4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()
import unittest
from test import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        num1 = [1,9,3,7,0,7,7,2,1]
        num2 = [-7,6,1.,8,3,8,2,5,7,2,8,7]
        self.assertEqual(multiply(num1, num2), [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7])

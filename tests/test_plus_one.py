import unittest
from tests import plus_one

class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        A = [1,2,9]
        self.assertEqual(plus_one(A), [1,3,0])

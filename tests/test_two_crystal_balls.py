import unittest
from tests import two_crystal_balls
import random

class TestBinarySearchList(unittest.TestCase):

    def test_two_crystal_balls(self):
        idx = random.randrange(0, 10000)
        data = [i >= idx for i in range(0, 10000)]

        self.assertEqual(two_crystal_balls(data), idx)
        self.assertEqual(two_crystal_balls([False for i in range(0, 821)]), -1)


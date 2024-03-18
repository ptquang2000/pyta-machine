import unittest
from test import linear_search

class TestLinearSearchList(unittest.TestCase):

    def test_linear_search(self):
        foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
        self.assertEqual(linear_search(foo, 69), True)
        self.assertEqual(linear_search(foo, 1336), False)
        self.assertEqual(linear_search(foo, 69420), True)
        self.assertEqual(linear_search(foo, 69421), False)
        self.assertEqual(linear_search(foo, 1), True)
        self.assertEqual(linear_search(foo, 0), False)

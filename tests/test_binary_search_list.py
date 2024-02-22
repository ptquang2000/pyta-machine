import unittest
from tests import binary_search

class TestBinarySearchList(unittest.TestCase):

    def test_binary_search(self):
        foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
        self.assertEqual(binary_search(foo, 69), True)
        self.assertEqual(binary_search(foo, 1336), False)
        self.assertEqual(binary_search(foo, 69420), True)
        self.assertEqual(binary_search(foo, 69421), False)
        self.assertEqual(binary_search(foo, 1), True)
        self.assertEqual(binary_search(foo, 0), False)

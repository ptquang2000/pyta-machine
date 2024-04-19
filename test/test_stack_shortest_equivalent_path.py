import unittest
from test import shortest_equivalent_path

class TestShortestEquivalentPath(unittest.TestCase):
    def test_shortest_equivalent_path(self):
        self.assertEqual(shortest_equivalent_path("/home/"), "/home")
        self.assertEqual(shortest_equivalent_path("/../"), "/")
        self.assertEqual(shortest_equivalent_path("/home//foo/"), "/home/foo")

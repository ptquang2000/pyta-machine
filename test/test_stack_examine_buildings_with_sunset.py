import unittest
from test import examine_buildings_with_sunset

class TestExamineBuildingsWithSunset(unittest.TestCase):
    def test_examine_buildings_with_sunset(self):
        self.assertEqual(examine_buildings_with_sunset([11, 12, 13, 14, 15]), [0, 1, 2, 3, 4])
        self.assertEqual(examine_buildings_with_sunset([7, 4, 8, 2, 9]), [0, 2, 4])

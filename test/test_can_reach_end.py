import unittest
from test import can_reach_end

class TestCanReachEnd(unittest.TestCase):
    def test_can_reach_end(self):
        self.assertEqual(can_reach_end([2,4,1,1,0,2,3]), True)
        self.assertEqual(can_reach_end([3,3,7,0,2,0,1]), True)
        self.assertEqual(can_reach_end([3,2,0,0,2,0,7]), False)

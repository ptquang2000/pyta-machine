from unittest import TestCase
from test import bt_in_order
from test.test_core_tree import tree

class TestBTInOrder(TestCase):
    def test_bt_in_order(self):
        self.assertEqual(bt_in_order(tree), [
            5,
            7,
            10,
            15,
            20,
            29,
            30,
            45,
            50,
            100,
        ]

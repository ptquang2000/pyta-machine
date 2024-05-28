from unittest import TestCase
from test import bt_post_order
from test.test_core_tree import tree

class TestBTPostOrder(TestCase):
    def test_bt_post_order(self):
        self.assertEqual(bt_post_order(tree), [
            7,
            5,
            15,
            10,
            29,
            45,
            30,
            100,
            50,
            20,
        ]

import unittest
from test import has_cycle
from common.list_node import *

class TestHasCycle(unittest.TestCase):
    def test_has_cycle(self):
        end = ListNode(-4)
        node = ListNode(0, end)
        expected = ListNode(2, node)
        L = ListNode(3, expected)
        end.next = expected
        result = has_cycle(L)
        self.assertEqual(id(result), id(expected))

        end = ListNode(2)
        expected = ListNode(1, end)
        end.next = expected
        result = has_cycle(L)
        self.assertEqual(id(result), id(expected))

        end = ListNode(2)
        self.assertEqual(has_cycle(end), None)

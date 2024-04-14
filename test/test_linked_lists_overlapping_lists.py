import unittest
from common.list_node import *
from test import overlapping_lists

class TestOverlappingLists(unittest.TestCase):
    def test_overlapping_lists(self):
        B = ListNode(0, None) 
        A = ListNode(0, B) 
        node = ListNode(0, A)
        node = ListNode(0, node)
        B.next = node
        node = ListNode(0, B)
        L1 = ListNode(0, node)
        L2 = A
        self.assertIn(overlapping_lists, [A, B])

        end = ListNode(-4, None)
        node = ListNode(0, end)
        expected = ListNode(2, node)
        L = ListNode(3, expected)
        end.next = expected
        result = has_cycle(L)
        self.assertIs(result, expected)

        end = ListNode(2, None)
        expected = ListNode(1, end)
        L = expected
        end.next = expected
        result = has_cycle(L)
        self.assertIs(result, expected)

        end = ListNode(2, None)
        self.assertIsNone(has_cycle(end))

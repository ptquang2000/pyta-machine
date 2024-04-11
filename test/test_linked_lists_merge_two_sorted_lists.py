import unittest
from test import merge_two_sorted_lists
from common.list_node import *

class TestMergeTwoSortedLists(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        node = ListNode(4)
        node = ListNode(2, node)
        L1 = ListNode(1, node)
        node = ListNode(4)
        node = ListNode(3, node)
        L2 = ListNode(1, node)
        head = merge_two_sorted_lists(L1, L2)
        result = list()
        while head:
            result.append(head.data)
            self.assertEqual(len(result) <= 6, True)
            head = head.next
        self.assertEqual(result, [1,1,2,3,4,4])

        node = ListNode(7)
        node = ListNode(5, node)
        L1 = ListNode(2, node)
        node = ListNode(11)
        L2 = ListNode(3, node)
        head = merge_two_sorted_lists(L1, L2)
        result = list()
        while head:
            result.append(head.data)
            self.assertEqual(len(result) <= 5, True)
            head = head.next
        self.assertEqual(result, [2,3,5,7,11])

        head = merge_two_sorted_lists(None, None)
        self.assertEqual(head, None)

        L2 = ListNode(0)
        head = merge_two_sorted_lists(None, L2)
        result = list()
        while head:
            result.append(head.data)
            self.assertEqual(len(result) <= 1, True)
            head = head.next
        self.assertEqual(result, [0])

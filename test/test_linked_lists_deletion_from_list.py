import unittest
from common.list_node import *
from test import deletion_from_list

class TestDeletionFromList(unittest.TestCase):
    def test_deletion_from_list(self):
        node = ListNode(9)
        node = ListNode(1, node)
        del_node = ListNode(5, node)
        L = ListNode(4, del_node)
        head = deletion_from_list(del_node)
        self.assertEqual(to_list(self, head, 3), [4,1,9])

        node = ListNode(9)
        del_node = ListNode(1, node)
        node = ListNode(5, del_node)
        L = ListNode(4, node)
        head = deletion_from_list(del_node)
        self.assertEqual(to_list(self, head, 3), [4,5,9])

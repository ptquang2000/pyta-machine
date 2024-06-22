from unittest import TestCase
from common.binary_node import BinaryNode, form_binary_tree
from test import find_kth_node_binary_tree

class TestFindKThNodeBinaryTree(TestCase):
    def test_find_kth_noed_binary_tree(self):
        self.assertEqual(find_kth_node_binary_tree(BinaryNode.cast(form_binary_tree([3,1,4,None,2])), 1).data, 1)
        self.assertEqual(find_kth_node_binary_tree(BinaryNode.cast(form_binary_tree([5,3,6,2,4,None,None,1])), 3).data, 3)


import unittest
from tests import DoublyLinkedList
from tests.test_list import test_list

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def test_list(self):
        test_list(self)


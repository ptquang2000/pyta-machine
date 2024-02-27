import unittest
from tests import TestList
from tests import ArrayList

class TestArrayList(TestList):
    def setUp(self):
        self.list = ArrayList(3)

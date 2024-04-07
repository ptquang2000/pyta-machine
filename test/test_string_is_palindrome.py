import unittest
from test import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal Panama."), True)
        self.assertEqual(is_palindrome("Able was I, ere I saw Elba!"), True)
        self.assertEqual(is_palindrome("Ray a Ray"), False)

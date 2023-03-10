import unittest

from Basic_Test import is_prime

# import the is_prime function

# Testing demo

class TestPrime(unittest.TestCase):
    def test_two(self):
        self.assertTrue(is_prime(2))
    def test_five(self):
        self.assertTrue(is_prime(5))
    def test_nine(self):
        self.assertFalse(is_prime(9))
    def test_eleven(self):
        self.assertTrue(is_prime(11))
if __name__=='__main__':
    unittest.main()
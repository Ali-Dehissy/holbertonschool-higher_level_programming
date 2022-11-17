#!/usr/bin/python3
"""Unitest max integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing positive output"""
    def test_positiveoutput(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    """Testing negative output"""
    def test_max_negativeoutput(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    """Testing if one number only"""
    def test_max_onenumber(self):
        self.assertEqual(max_integer([3]), 3)
    """Testing for one negative number"""
    def test_max_onenegativenumber(self):
        self.assertEqual(max_integer([-1]), -1)
    """Testing if unordered list"""
    def test_max_unordered(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
    """Testing if identical values"""
    def test_max_identicalvalues(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
    """Testing for strings"""
    def test_max_strings(self):
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
    """Tessting raising error """
    def test_max_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)
    """Testing for true"""
    def test_max_True(self):
        with self.assertRaises(TypeError):
            max_integer(True)
    """Testing if empty list exists"""
    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""
    def test_empty(self):
        """Test for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test for a list with a single element."""
        self.assertEqual(max_integer([42,]), 42)

    def test_positive_numbers(self):
        """Test for a list with positive numbers."""
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test for negative numbers in the list."""
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_duplicate_numbers(self):
        """Test for a list with duplicate numbers."""
        self.assertEqual(max_integer([3, 3, 4, 3]), 4)

    def test_type(self):
        """raises TypeError if not an integer."""
        with self.assertRaises(TypeError):
            max_integer([1, 5, 3, "alx"])

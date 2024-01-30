#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""
    def test_empty(self):
        """Testing if empty list."""
        self.assertIsNone(max_integer([]))

    def test_no_arguments(self):
        """Testing when no arguments."""
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test for a list with a single element."""
        self.assertEqual(max_integer([42, ]), 42)

    def test_positive_numbers(self):
        """Testing all positive numbers."""
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Testing all negative numbers."""
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_positive_numbers(self):
        """Testing both positive and negative numbers."""
        self.assertEqual(max_integer([-1, 3, -2, 4]), 4)

    def test_duplicate_numbers(self):
        """Testing repeated numbers."""
        self.assertEqual(max_integer([3, 3, 1, 3]), 3)

    def test_type(self):
        """raises TypeError if an element is not int."""
        with self.assertRaises(TypeError):
            max_integer([1, 5, 3, "alx"])

    def test_list_strings(self):
        """Testing a list of strings."""
        self.assertEqual(max_integer(["alx", "heba", "zaki"]), "zaki")

    def test_list_of_single_string(self):
        """Testing list with a single string."""
        self.assertEqual(max_integer(["alx"]), "alx")

    def test_floats(self):
        """Testing a list of floats."""
        self.assertEqual(max_integer([1.5, 3.2, 2.7]), 3.2)

    def test_list_with_none(self):
        """Testing a list containing None."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])

    def test_list_with_nan(self):
        """Testing a list containing NaN."""
        self.assertEqual(max_integer([1, float('nan'), 3, 4]), 4)

    def test_list_with_inf(self):
        """Testing a list containing inf."""
        self.assertEqual(max_integer([1, 2, float('inf'), 4]), float('inf'))

    def test_numeric_types(self):
        """Testing list with mixed numeric types."""
        self.assertEqual(max_integer([1, 2.5, 3, 4]), 4)


if __name__ == '__main__':
    unittest.main()

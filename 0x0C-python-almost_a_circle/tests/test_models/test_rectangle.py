#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle function."""
    def test_id_with_incremet(self):
        """Test when ID is none and we increment the object."""
        b1 = Rectangle(10, 2)
        b2 = Rectangle(2, 10)
        b3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
   


if __name__ == '__main__':
    unittest.main()

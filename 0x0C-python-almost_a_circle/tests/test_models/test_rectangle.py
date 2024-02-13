#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle function."""
    
   
    def test_init(self):
        # Test initialization
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

        # Test initialization with custom values
        rect = Rectangle(3, 7, 2, 4, 1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 1)

    def test_width_validation(self):
        # Test width validation
        with self.assertRaises(TypeError):
            Rectangle("alx", 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(-5, 5)

    def test_height_validation(self):
        # Test height validation
        with self.assertRaises(TypeError):
            Rectangle(5, "alx")
        with self.assertRaises(ValueError):
            Rectangle(5, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, -5)

    def test_x_validation(self):
        # Test x validation
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid")
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1)

    def test_y_validation(self):
        # Test y validation
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "invalid")
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -1)

    def test_area(self):
        # Test area calculation
        rect = Rectangle(3, 5)
        self.assertEqual(rect.area(), 15)

    def test_display(self):
        # Test display
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        r3 = Rectangle(3, 2)
        r3.display()
        r4 = Rectangle(3, 2, 1)
        r4.display()

    def test_str(self):
        # Test string representation
        rect = Rectangle(4, 8, 1, 2, 7)
        self.assertEqual(str(rect), "[Rectangle] (7) 1/2 - 4/8")

    def test_update(self):
        # Test update method
        rect = Rectangle(2, 3)
        rect.update(5, 6, 7, 8, 9)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 9)

    def test_to_dictionary(self):
        # Test to_dictionary method
        rect = Rectangle(4, 6, 2, 2, 10)
        self.assertEqual(rect.to_dictionary(), {'x': 2, 'y': 2, 'id': 10,
                                                 'height': 6, 'width': 4})



if __name__ == '__main__':
    unittest.main()

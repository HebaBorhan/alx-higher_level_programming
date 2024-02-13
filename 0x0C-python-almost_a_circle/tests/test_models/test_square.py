#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
from models.square import Square
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """Unit tests for the Square function."""
    
   
    def test_init(self):
        # Test initialization
        s1 = Square(5, 10)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        # Test initialization with custom values
        rect = Square(3, 7, 2, 4, 1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 1)

    def test_width_validation(self):
        # Test width validation
        with self.assertRaises(TypeError):
            Square("alx", 5)
        with self.assertRaises(ValueError):
            Square(0, 5)
        with self.assertRaises(ValueError):
            Square(-5, 5)

    def test_height_validation(self):
        # Test height validation
        with self.assertRaises(TypeError):
            Square(5, "alx")
        with self.assertRaises(ValueError):
            Square(5, 0)
        with self.assertRaises(ValueError):
            Square(5, -5)

    def test_x_validation(self):
        # Test x validation
        with self.assertRaises(TypeError):
            Square(5, 10, "invalid")
        with self.assertRaises(ValueError):
            Square(5, 10, -1)

    def test_y_validation(self):
        # Test y validation
        with self.assertRaises(TypeError):
            Square(5, 10, 2, "invalid")
        with self.assertRaises(ValueError):
            Square(5, 10, 2, -1)

    def test_area(self):
        # Test area calculation
        s1 = Square(3, 5)
        self.assertEqual(s1.area(), 15)

    def test_display(self):
        # Test display
        s1 = Square(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            s1.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

        s2 = Square(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            s2.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

        s3 = Square(3, 2)
        expected_output = "###\n###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            s3.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

        s4 = Square(3, 2, 1)
        expected_output = " ###\n ###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            s4.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_str(self):
        # Test string representation
        s1 = Square(4, 8, 1, 2, 7)
        self.assertEqual(str(s1), "[Square] (7) 1/2 - 4/8")

    def test_update(self):
        # Test update method
        s1 = Square(2, 3)
        s1.update(5, 6, 7, 8, 9)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 6)
        self.assertEqual(s1.height, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

    def test_to_dictionary(self):
        # Test to_dictionary method
        s1 = Square(4, 6, 2, 2, 10)
        self.assertEqual(s1.to_dictionary(), {'x': 2, 'y': 2, 'id': 10,
                                                 'height': 6, 'width': 4})

if __name__ == '__main__':
    unittest.main()

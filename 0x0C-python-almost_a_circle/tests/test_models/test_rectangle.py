#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import os
from contextlib import redirect_stdout


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
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            r2.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

        r3 = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            r3.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

        r4 = Rectangle(3, 2, 1)
        expected_output = " ###\n ###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            r4.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

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

    def test_create(self):
        """Test creation of Rectangle instances."""
        # Test create method with various attributes
        rect1 = Rectangle.create(**{ 'id': 89 })
        rect2 = Rectangle.create(**{ 'id': 89, 'width': 1 })
        rect3 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        rect4 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        rect5 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })

        # Check if instances are created
        self.assertIsInstance(rect1, Rectangle)
        self.assertIsInstance(rect2, Rectangle)
        self.assertIsInstance(rect3, Rectangle)
        self.assertIsInstance(rect4, Rectangle)
        self.assertIsInstance(rect5, Rectangle)

    def test_save_to_file(self):
        """Test save_to_file method."""
        # Test save_to_file with different inputs
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

    def test_load_from_file(self):
        """Test load_from_file method."""
        # Test load_from_file when file doesn’t exist
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

        # Test load_from_file when file exists
        Rectangle.save_to_file([Rectangle(1, 2)])
        rectangles = Rectangle.load_from_file()
        self.assertTrue(len(rectangles) > 0)
        os.remove("Rectangle.json")

    def test_to_json_string_empty_list(self):
        """Test of Base.to_json_string([]) exists"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_data(self):
        """Test of Base.to_json_string([{ 'id': 12 }]) returning a string exists"""
        self.assertIsInstance(Base.to_json_string([{ 'id': 12 }]), str)


if __name__ == '__main__':
    unittest.main()

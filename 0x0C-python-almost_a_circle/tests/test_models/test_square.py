import unittest
from models.square import Square
from models.rectangle import Rectangle
import io
import os
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """Unit tests for the Square function."""
    
   
    def test_init(self):
        # Test initialization
        s1 = Square(5, 10)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 0)

        # Test initialization with custom values
        s2 = Square(3, 7, 2, 4)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 7)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 4)

    def test_width_validation(self):
        # Test width validation
        with self.assertRaises(TypeError):
            Square("alx")
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)

    def test_x_validation(self):
        # Test x validation
        with self.assertRaises(TypeError):
            Square(5, 10, "alx")
        with self.assertRaises(ValueError):
            Square(5, 10, -1)
        with self.assertRaises(TypeError):
            Square(5, "alx")
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_y_validation(self):
        # Test y validation
        with self.assertRaises(TypeError):
            Square(5, 10, "alx")
        with self.assertRaises(ValueError):
            Square(5, 10, -1)

    def test_area(self):
        # Test area calculation
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_display(self):
        # Test display
        s1 = Square(2, 3, 2)
        expected_output = "\n\n   ##\n   ##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            s1.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

        s2 = Square(3, 2, 1)
        expected_output = "\n  ###\n  ###\n  ###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            s2.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_str(self):
        # Test string representation
        s1 = Square(3, 1, 3, 3)
        self.assertEqual(str(s1), "[Square] (3) 1/3 - 3")

    def test_to_dictionary(self):
        # Test to_dictionary method
        s1 = Square(10, 2, 1, 9)
        self.assertEqual(s1.to_dictionary(), {'id': 9, 'x': 2, 'size': 10, 'y': 1})

    def test_update(self):
        # Test update method
        s = Square(2)
        s.update(5, 6, 7, 8)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)

    def test_create_with_id(self):
        """Test of Square.create(**{ 'id': 89 }) in Square exists"""
        square = Square.create(**{ 'id': 89 })
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 89)

    def test_create_with_id_and_size(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1 }) in Square exists"""
        square = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_create_with_id_size_x(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square exists"""
        square = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_create_with_id_size_x_y(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square exists"""
        square = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_save_to_file(self):
        """Test of Square.save_to_file(None) in Square exists"""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_load_from_file(self):
        """Test of Square.load_from_file() when file doesn’t exist exists"""
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

        """Test of Square.load_from_file() when file exists exists"""
        Square.save_to_file([Square(1)])
        squares = Square.load_from_file()
        self.assertTrue(len(squares) > 0)
        os.remove("Square.json")

    def test_save_to_file_with_empty_list(self):
        """Test of Square.save_to_file([]) in Square exists"""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove("Square.json")

if __name__ == '__main__':
    unittest.main()

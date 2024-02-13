import unittest
from models.square import Square
from models.rectangle import Rectangle
import io
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

if __name__ == '__main__':
    unittest.main()

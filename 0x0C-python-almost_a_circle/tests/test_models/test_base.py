import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for the Base function."""
    def test_id_with_incremet(self):
        """Test of ID."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_to_json_string_none(self):
        """Test of Base.to_json_string(None) exists"""
        self.assertIsNotNone(Base.to_json_string(None))

    def test_to_json_string_empty_list(self):
        """Test of Base.to_json_string([]) exists"""
        self.assertIsNotNone(Base.to_json_string([]))

    def test_to_json_string_with_data(self):
        """Test of Base.to_json_string([{ 'id': 12 }]) exists"""
        self.assertIsNotNone(Base.to_json_string([{ 'id': 12 }]))

    def test_to_json_string_returning_string(self):
        """Test of Base.to_json_string([{ 'id': 12 }]) returning a string exists"""
        self.assertIsInstance(Base.to_json_string([{ 'id': 12 }]), str)

    def test_from_json_string_none(self):
        """Test of Base.from_json_string(None) exists"""
        self.assertIsNotNone(Base.from_json_string(None))

    def test_from_json_string_empty_string(self):
        """Test of Base.from_json_string("[]") exists"""
        self.assertIsNotNone(Base.from_json_string("[]"))

    def test_from_json_string_with_data(self):
        """Test of Base.from_json_string('[{ "id": 89 }]') exists"""
        self.assertIsNotNone(Base.from_json_string('[{ "id": 89 }]'))

    def test_from_json_string_returning_list(self):
        """Test of Base.from_json_string('[{ "id": 89 }]') returning a list exists"""
        self.assertIsInstance(Base.from_json_string('[{ "id": 89 }]'), list)

if __name__ == '__main__':
    unittest.main()

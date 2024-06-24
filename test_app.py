# test_app.py
import unittest
from app import add_numbers, subtract_numbers

class TestMathFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(8, 2), 6)
        self.assertEqual(subtract_numbers(5, 5), 0)
        self.assertEqual(subtract_numbers(1, -1), 2)

if __name__ == "__main__":
    unittest.main()

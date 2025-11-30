import unittest
import math
from calculator import calculate_square_area, calculate_circle_area, calculate_triangle_area

class TestCalculator(unittest.TestCase):

    def test_calculate_square_area_valid(self):
        self.assertEqual(calculate_square_area(5), 25)
        self.assertEqual(calculate_square_area(0), 0)
        self.assertEqual(calculate_square_area(2.5), 6.25)

    def test_calculate_square_area_invalid(self):
        self.assertEqual(calculate_square_area(-1), "Error: Side length cannot be negative.")
        self.assertEqual(calculate_square_area(-5), "Error: Side length cannot be negative.")

    def test_calculate_circle_area_valid(self):
        self.assertAlmostEqual(calculate_circle_area(10), math.pi * 100)
        self.assertEqual(calculate_circle_area(0), 0)

    def test_calculate_circle_area_invalid(self):
        self.assertEqual(calculate_circle_area(-1), "Error: Radius cannot be negative.")

    def test_calculate_triangle_area_valid(self):
        self.assertEqual(calculate_triangle_area(6, 4), 12.0)
        self.assertEqual(calculate_triangle_area(10, 5), 25.0)
        self.assertEqual(calculate_triangle_area(0, 5), 0)

    def test_calculate_triangle_area_invalid(self):
        self.assertEqual(calculate_triangle_area(-1, 5), "Error: Base and height cannot be negative.")
        self.assertEqual(calculate_triangle_area(5, -1), "Error: Base and height cannot be negative.")
        self.assertEqual(calculate_triangle_area(-1, -1), "Error: Base and height cannot be negative.")

if __name__ == '__main__':
    unittest.main()

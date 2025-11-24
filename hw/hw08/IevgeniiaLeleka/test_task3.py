import unittest
from unittest.mock import patch
from task3 import area_calculator
from math import pi, pow

class TestAreaCalculator(unittest.TestCase):

    @patch("builtins.input", side_effect=["rectangle", "5", "3"])
    def test_rectangle_area(self, mock_input):
        result = area_calculator()
        self.assertEqual(result, 5 * 3)

    @patch("builtins.input", side_effect=["triangle", "4", "6"])
    def test_triangle_area(self, mock_input):
        result = area_calculator()
        self.assertEqual(result, 0.5 * 4 * 6)

    @patch("builtins.input", side_effect=["circle", "7"])
    def test_circle_area(self, mock_input):
        result = area_calculator()
        self.assertEqual(result, pi * pow(7, 2))

    @patch("builtins.input", side_effect=["hexagon"])
    def test_invalid_shape(self, mock_input):
        result = area_calculator()
        self.assertEqual(result, "Enter a valid shape")

if __name__ == "__main__":
    unittest.main()

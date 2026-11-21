
import unittest
from unittest.mock import patch

from app import count_symbols, count_vowels, divide, Figure


class TestFunctions(unittest.TestCase):

    def test_count_symbols(self):
        self.assertEqual(3, count_symbols("abc"))

    def test_count_symbols_empty(self):
        self.assertEqual(0, count_symbols(""))

    def test_count_symbols_ukrainian(self):
        self.assertEqual(7, count_symbols("Привіт!"))

    def test_count_vowels(self):
        self.assertEqual(3, count_vowels("молоко"))

    def test_count_vowels_empty(self):
        self.assertEqual(0, count_vowels(""))

    def test_count_vowels_digits(self):
        self.assertEqual(0, count_vowels("12345"))

    def test_count_vowels_ukrainian(self):
        self.assertEqual(3, count_vowels("молоко"))

    def test_divide(self):
        self.assertEqual(2, divide(10, 5))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


class TestFigure(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.figure_types = [
            "квадрат",
            "прямокутник",
            "трикутник"
        ]

    @classmethod
    def tearDownClass(cls):
        cls.figure_types = []

    def setUp(self):
        self.figure = Figure("квадрат", 5)

    def tearDown(self):
        self.figure = None

    def test_figure_type(self):
        self.assertEqual(
            "квадрат",
            self.figure.get_figure_type()
        )

    def test_figure_length(self):
        self.assertEqual(
            5,
            self.figure.get_figure_length()
        )

    def test_square_angles(self):
        self.assertEqual(
            4,
            Figure("квадрат", 5).get_angles()
        )

    def test_rectangle_angles(self):
        self.assertEqual(
            4,
            Figure("прямокутник", 5).get_angles()
        )

    def test_triangle_angles(self):
        self.assertEqual(
            3,
            Figure("трикутник", 5).get_angles()
        )

    def test_all_figure_types(self):
        for figure_type in self.figure_types:
            with self.subTest(figure_type=figure_type):
                figure = Figure(figure_type, 5)
                self.assertEqual(
                    figure_type,
                    figure.get_figure_type()
                )

    def test_unknown_figure(self):
        with self.assertRaises(ValueError):
            Figure("коло", 5).get_angles()

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", -5)

    def test_zero_length(self):
        self.assertEqual(
            0,
            Figure("квадрат", 0).get_figure_length()
        )


class TestMock(unittest.TestCase):

    @patch("builtins.input", return_value="5")
    def test_input(self, mock_input):
        result = input("Введіть число: ")

        self.assertEqual("5", result)
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)

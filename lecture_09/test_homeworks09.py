import unittest
from homeworks import *

class MyTest(unittest.TestCase):

    def test_two_digits_sum(self):
        result = two_digits_sum(4, 17)
        self.assertEqual(21, result)  # Check that function returns correct sum of 2 digits

    def test_positive_and_negative_digits_sum(self):
        result = two_digits_sum(4, -5)
        self.assertEqual(-1, result)  # Check that function returns correct sum of 2 digits if one digit with minus sign

    def test_calculate_average_for_empty_list(self):
        self.assertIsNone(calculate_average([]))  # Check that function returns None for an empty list

    def test_calculate_average_for_not_empty_list(self):
        result = calculate_average([10, 2, 3, 4, 5])
        self.assertEqual(4.8, result)  # Check that function returns average for not empty list

    def test_reverse_returns_reversed_string(self):
        self.assertEqual(reverse("Hello, World"), "dlroW ,olleH")  # Check that function returns the reversed string

    def test_reverse_returns_empty_string_for_empty_input(self):
        self.assertEqual(reverse(""), "")  # Check that function returns an empty string when the input is empty

    def test_longest_word_returns_longest_word(self):
        self.assertEqual(longest_word(['pen', 'pencil', 'book', 'notebook', 'ruler', 'dictionary', 'marker']),
                         'dictionary')  # Check that function returns the longest word

    def test_longest_word_returns_none_for_empty_list(self):
        self.assertIsNone(longest_word([]))  # Check that function returns None for an empty list

    def test_sum_of_even_numbers_in_list_returns_correct_sum(self):
        result = sum_of_even_numbers_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(30, result)  # Check that function returns the correct sum

    def test_sum_of_even_numbers_in_list_returns_zero_for_empty_list(self):
        self.assertEqual(sum_of_even_numbers_in_list([]), 0)  # Check that function returns 0 for an empty list


if __name__ == '__main__':
    unittest.main()

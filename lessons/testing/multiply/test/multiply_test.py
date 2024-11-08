import unittest

from lessons.testing.multiply.multiply import *


class MultiPlication(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        result = multiply(5, 4)
        self.assertEqual(result, 20)

    def test_multiply_negative_positive(self):
        result = multiply(5, -4)
        self.assertEqual(result, -20)

    def test_pos_pos(self):
        result = multiply(-5,-4)
        self.assertNotEqual(result, -15)

    def test_multiply_string(self):
        result = multiply("a",5)
        self.assertFalse(result)

class AllExceptions(unittest.TestCase):
    def test_all_cases(self):
        self.assertEqual(10, add(5, 5))  # Passes if add(5, 5) equals 10
        self.assertTrue(result)  # Passes if result is True
        self.assertFalse(error)  # Passes if error is False
        self.assertIs(result, expected_result)  # Passes if result is expected_result (same object)
        self.assertIsNone(result)  # Passes if result is None
        self.assertIsNotNone(result)  # Passes if result is not None
        self.assertIn(item, my_list)  # Passes if item is present in my_list
        self.assertNotIn(item, my_list)  # Passes if item is not present in my_list
        self.assertRaises(ValueError, divide, 10, 0)  # Passes if calling divide(10, 0) raises ValueError
        self.assertAlmostEqual(result, expected_result,
                               places=2)  # Passes if result and expected_result are approximately equal up to 2 decimal places



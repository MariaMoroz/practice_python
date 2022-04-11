import unittest
from homework.hw_5 import compare_numbers
from homework.hw_5 import compare_input_positive_numbers
from homework.hw_7 import get_text

class test_cases(unittest.TestCase):
    def test_compare_equals_numbers(self):
        self.assertFalse(compare_numbers(5,5))
    def test_compare_numbers_positive(self):
        self.assertTrue(compare_numbers(5,3))
    def test_compare_positive_numbers(self):
        self.assertEqual(compare_input_positive_numbers(-5,3), "Can compare only positive numbers!")
    def test_compare_positive_numbers(self):
        self.assertEqual(compare_input_positive_numbers(5,3), True)
    def test_get_text(self):
        self.assertEqual(get_text('abc'), "abc")

if __name__ == '__main__':
    unittest.main()
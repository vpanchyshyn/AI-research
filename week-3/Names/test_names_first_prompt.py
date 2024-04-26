"""Тестування написане ChatGPT після надання умови завдання. Нелогічні тести, що практично не покривають жодних граничних випадків."""

import unittest
import solution

class TestFindNames(unittest.TestCase):
    def test_empty_file(self):
        result = solution.find_names("empty_file.txt")
        self.assertEqual(result, (set(), (0, set()), ('', 0, 0)))

    def test_single_name(self):
        result = solution.find_names("single_name.txt")
        self.assertEqual(result, ({'John'}, (0, set()), ('J', 1, 10)))

    def test_multiple_names(self):
        result = solution.find_names("multiple_names.txt")
        expected_top_names = {'John', 'Alice', 'Bob'}
        expected_unique_names = (2, {'Kate', 'Mary'})
        expected_most_common_letter = ('A', 2, 25)
        self.assertEqual(result, (expected_top_names, expected_unique_names, expected_most_common_letter))

if __name__ == '__main__':
    unittest.main()

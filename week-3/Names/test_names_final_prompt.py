"""Тестування написане ChatGPT після надання умови завдання та прикладу файлу, 
який необхідно опрацювати. В певній мірі закладена правильна логіка у самих тестах, 
та через невірний аналіз файлу конкретні приклади невідповідають дійсності."""
import unittest
import names

class TestFindNames(unittest.TestCase):
    def test_three_most_popular_names(self):
        result = names.find_names("boy_names.txt")
        expected_top_names = {'МАТВІЙ', 'МАКСИМ', 'ДАВИД'}
        self.assertEqual(result[0], expected_top_names)

    def test_unique_names(self):
        result = names.find_names("boy_names.txt")
        expected_unique_names = (18, {'АВЕТ', 'АВІВ', 'АЛЬМАНСУР', 'БАҐРАМ', 'БОББІ', 'ГЕНРІ', 'ЄН', 'ЖДАН', 'КАМІЛЬ', 'ЛЕАНДРО', 'МАРЕК', 'МАССІНІССА', 'ОКТАВІАН', 'ПАУЛО', 'ПИЛИП', 'СНАТІСЛАВ', 'ТАРА', 'ФІЛІП'})
        self.assertEqual(result[1], expected_unique_names)

    def test_most_common_letter(self):
        result = names.find_names("boy_names.txt")
        expected_most_common_letter = ('М', 1176, 2230)
        self.assertEqual(result[2], expected_most_common_letter)

if __name__ == '__main__':
    unittest.main()

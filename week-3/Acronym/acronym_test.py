import unittest
from acronym import create_acronym
class TestCreateAcronym(unittest.TestCase):
    def test_create_acronym_english(self):
        message = "random access memory\nAs soon As possible"
        expected_output = "RAM - random access memory\nASAP - As soon As possible"
        self.assertEqual(create_acronym(message), expected_output)

    def test_create_acronym_ukrainian(self):
        message = "Дуже цікавий тест\nПокрокове розв'язання"
        expected_output = "ДЦТ - Дуже цікавий тест\nПР - Покрокове розв'язання"
        self.assertEqual(create_acronym(message), expected_output)

    def test_create_acronym_empty_message(self):
        message = ""
        self.assertIsNone(create_acronym(message))

    def test_create_acronym_invalid_input(self):
        message = "Not a valid phrase\n123"
        self.assertIsNone(create_acronym(message))

if __name__ == '__main__':
    unittest.main()

#general tests generated based on text question with all the rules provided
import unittest
from validator import Validator

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_name_surname(self):
        # Test cases for validate_name_surname method
        self.assertTrue(self.validator.validate_name_surname("John Doe"))
        self.assertTrue(self.validator.validate_name_surname("Alice Smith"))
        # Edge cases
        self.assertFalse(self.validator.validate_name_surname("john doe"))  # First letter not uppercase
        self.assertFalse(self.validator.validate_name_surname("JohnDoe"))   # No space between name and surname
        self.assertFalse(self.validator.validate_name_surname("J"))         # Name too short
        self.assertFalse(self.validator.validate_name_surname("John Doe "*10)) # Name too long
        self.assertFalse(self.validator.validate_name_surname("123 456"))   # Contains digits
        self.assertFalse(self.validator.validate_name_surname("!@#$ %^&")) # Contains punctuation

    def test_validate_age(self):
        # Test cases for validate_age method
        self.assertTrue(self.validator.validate_age("25"))
        self.assertTrue(self.validator.validate_age("50"))
        # Edge cases
        self.assertFalse(self.validator.validate_age("15"))  # Age too young
        self.assertFalse(self.validator.validate_age("100")) # Age too old
        self.assertFalse(self.validator.validate_age("abc")) # Invalid characters

    def test_validate_country(self):
        # Test cases for validate_country method
        self.assertTrue(self.validator.validate_country("Ukraine"))
        self.assertTrue(self.validator.validate_country("France"))
        # Edge cases
        self.assertFalse(self.validator.validate_country("ukraine"))     # First letter not uppercase
        self.assertFalse(self.validator.validate_country("Ukr123"))      # Contains digits
        self.assertFalse(self.validator.validate_country("A"*11))         # Too long
        self.assertFalse(self.validator.validate_country("A"))            # Too short

    def test_validate_region(self):
        # Test cases for validate_region method
        self.assertTrue(self.validator.validate_region("Lviv123"))
        self.assertTrue(self.validator.validate_region("Kharkiv"))
        # Edge cases
        self.assertFalse(self.validator.validate_region("123Lviv"))      # Contains digits at the start
        self.assertFalse(self.validator.validate_region("Kh@rkiv"))       # Contains special characters
        self.assertFalse(self.validator.validate_region("A"*21))          # Too long

    def test_validate_living_place(self):
        # Test cases for validate_living_place method
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 2a"))
        self.assertTrue(self.validator.validate_living_place("Example av. 11"))
        # Edge cases
        self.assertFalse(self.validator.validate_living_place("123 Main St."))  # Street name contains digits
        self.assertFalse(self.validator.validate_living_place("St. 123 2A"))    # Street name contains digits
        self.assertFalse(self.validator.validate_living_place("Koselnytska 2a")) # Missing street type
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. a")) # Missing building number
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 12AA")) # Invalid building number format

    def test_validate_index(self):
        # Test cases for validate_index method
        self.assertTrue(self.validator.validate_index("12345"))
        self.assertTrue(self.validator.validate_index("67890"))
        # Edge cases
        self.assertFalse(self.validator.validate_index("123456"))    # Too long
        self.assertFalse(self.validator.validate_index("abcde"))     # Invalid characters
        self.assertFalse(self.validator.validate_index("1 2345"))    # Contains whitespace

    def test_validate_phone(self):
        # Test cases for validate_phone method
        self.assertTrue(self.validator.validate_phone("+380951234567"))
        self.assertTrue(self.validator.validate_phone("+38 (095) 123-45-67"))
        # Edge cases
        self.assertFalse(self.validator.validate_phone("0951234567"))           # Missing country code
        self.assertFalse(self.validator.validate_phone("+3801234567890"))       # Too many digits
        self.assertFalse(self.validator.validate_phone("+38 (095) 12345678"))   # Missing hyphens
        self.assertFalse(self.validator.validate_phone("+38 (095) 12X-45-67"))  # Invalid character in local part

    def test_validate_email(self):
        # Test cases for validate_email method
        self.assertTrue(self.validator.validate_email("user@example.com"))
        self.assertTrue(self.validator.validate_email("someone@ucu.edu.ua"))
        # Edge cases
        self.assertFalse(self.validator.validate_email("user@.com"))           # Missing domain
        self.assertFalse(self.validator.validate_email("user@example"))        # Missing type
        self.assertFalse(self.validator.validate_email("@example.com"))         # Missing username
        self.assertFalse(self.validator.validate_email("user@domain"))          # Missing type
        self.assertFalse(self.validator.validate_email("user@domain."))         # Missing type
        self.assertFalse(self.validator.validate_email("user@@example.com"))    # Double "@" symbol
        self.assertFalse(self.validator.validate_email("user@domain@.com"))     # Double "@" symbol
        self.assertFalse(self.validator.validate_email("user@domain.com@"))     # Double "@" symbol
        self.assertFalse(self.validator.validate_email("user@example.com."))    # Extra dot in type
        self.assertFalse(self.validator.validate_email("user@domain@com"))     # Missing dot in type

    def test_validate_id(self):
        # Test cases for validate_id method
        self.assertTrue(self.validator.validate_id("102345"))
        # Edge cases
        self.assertFalse(self.validator.validate_id("123456"))      # No zero
        self.assertFalse(self.validator.validate_id("1023045"))     # Multiple zeros
        self.assertFalse(self.validator.validate_id("abc000"))      # Invalid characters

    def test_validate(self):
        # Test cases for validate method
        valid_data = "John Doe,25,Ukraine,Lviv,Koselnytska st. 2a,12345,+380951234567,user@example.com,102345"
        invalid_data_short = "John Doe,25,Ukraine,Lviv,Koselnytska st. 2a,12345,+380951234567,user@example.com"  # Missing id
        invalid_data_long = "John Doe,25,Ukraine,Lviv,Koselnytska st. 2a,12345,+380951234567,user@example.com,102345,extra"  # Extra data

        self.assertTrue(self.validator.validate(valid_data))
        self.assertFalse(self.validator.validate(invalid_data_short))
        self.assertFalse(self.validator.validate(invalid_data_long))
if __name__ == "__main__":
    unittest.main()

#correct test cases after the request to write tests for every method separately
#including all rules and conditions

import unittest
from validator import Validator

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_name_surname_two_words(self):
        # Test cases for validate_name_surname method - should be only 2 words
        self.assertTrue(self.validator.validate_name_surname("John Doe"))
        self.assertTrue(self.validator.validate_name_surname("Alice Smith"))
        # Edge cases
        self.assertFalse(self.validator.validate_name_surname("John"))         # Only one word
        self.assertFalse(self.validator.validate_name_surname("John Alex Doe")) # More than two words

    def test_validate_name_surname_first_uppercase(self):
        # Test cases for validate_name_surname method - should be only first uppercase letter in name and surname
        self.assertTrue(self.validator.validate_name_surname("John Doe"))
        self.assertTrue(self.validator.validate_name_surname("Alice Smith"))
        # Edge cases
        self.assertFalse(self.validator.validate_name_surname("john doe"))    # First letter not uppercase
        self.assertFalse(self.validator.validate_name_surname("John doe"))    # Surname first letter not uppercase
        self.assertFalse(self.validator.validate_name_surname("JOhn DOe"))    # Random case

    def test_validate_name_surname_size(self):
        # Test cases for validate_name_surname method - size of both name and surname should be between 2 and 30
        self.assertTrue(self.validator.validate_name_surname("John Doe"))
        self.assertTrue(self.validator.validate_name_surname("Alice Smith"))
        # Edge cases
        self.assertFalse(self.validator.validate_name_surname("J"))              # Name too short
        self.assertFalse(self.validator.validate_name_surname("A"*31))           # Name too long
        self.assertFalse(self.validator.validate_name_surname("JohnDoe"*10))    # Name too long

    def test_validate_name_surname_no_digits_punctuation(self):
        # Test cases for validate_name_surname method - no digits or punctuation in name or surname
        self.assertTrue(self.validator.validate_name_surname("John Doe"))
        self.assertTrue(self.validator.validate_name_surname("Alice Smith"))
        # Edge cases
        self.assertFalse(self.validator.validate_name_surname("John2 Doe"))      # Name contains digits
        self.assertFalse(self.validator.validate_name_surname("Alice, Smith"))   # Name contains punctuation
        self.assertFalse(self.validator.validate_name_surname("Joh@n Doe"))      # Name contains special characters


    def test_validate_age_valid_range(self):
        # Test cases for validate_age method - valid age is a number between 16 and 99
        self.assertTrue(self.validator.validate_age("25"))
        self.assertTrue(self.validator.validate_age("50"))
        # Edge cases
        self.assertTrue(self.validator.validate_age("16"))   # Minimum valid age
        self.assertTrue(self.validator.validate_age("99"))   # Maximum valid age

    def test_validate_age_invalid_range(self):
        # Test cases for validate_age method - valid age is a number between 16 and 99
        self.assertFalse(self.validator.validate_age("15"))  # Age too young
        self.assertFalse(self.validator.validate_age("100")) # Age too old
        self.assertFalse(self.validator.validate_age("-5"))  # Negative age
        self.assertFalse(self.validator.validate_age("abc")) # Invalid characters

    def test_validate_country(self):
        # Test cases for validate_country method
        self.assertTrue(self.validator.validate_country("Ukraine"))
        self.assertTrue(self.validator.validate_country("France"))
        # Edge cases
        self.assertTrue(self.validator.validate_country("A"*10))      # Maximum length
        self.assertFalse(self.validator.validate_country("ukraine"))   # First letter not uppercase
        self.assertFalse(self.validator.validate_country("123Country")) # Contains digits
        self.assertFalse(self.validator.validate_country(""))           # Empty string

    def test_validate_region(self):
        # Test cases for validate_region method
        self.assertTrue(self.validator.validate_region("Lviv123"))
        self.assertTrue(self.validator.validate_region("Kharkiv"))
        # Edge cases
        self.assertTrue(self.validator.validate_region("A"*10))       # Maximum length
        self.assertFalse(self.validator.validate_region("123Region"))  # Contains digits
        self.assertFalse(self.validator.validate_region(""))            # Empty string

    def test_validate_living_place_format(self):
        # Test cases for validate_living_place method - should be in the format "Koselnytska st. 2a"
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 2a"))
        # Edge cases
        self.assertFalse(self.validator.validate_living_place("Koselnytska street 2a"))  # Incorrect format
        self.assertFalse(self.validator.validate_living_place("Koselnytska 2a"))         # Incorrect format

    def test_validate_living_place_street_name(self):
        # Test cases for validate_living_place method - name of street should be between 3 and 20 chars,
        # first character uppercase, no digits in it
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 2a"))
        # Edge cases
        self.assertFalse(self.validator.validate_living_place("Main St. 2a"))    # Street name too short
        self.assertFalse(self.validator.validate_living_place("Longest Street Ever St. 2a"))  # Street name too long
        self.assertFalse(self.validator.validate_living_place("123 Street 2a"))   # Street name contains digits
        self.assertFalse(self.validator.validate_living_place("street 2a"))       # Street name not capitalized

    def test_validate_living_place_street_type(self):
        # Test cases for validate_living_place method - type of street should be "st.", "av.", "prosp." or "rd."
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 2a"))
        # Edge cases
        self.assertFalse(self.validator.validate_living_place("Koselnytska street 2a"))  # Incorrect street type
        self.assertFalse(self.validator.validate_living_place("Koselnytska ave. 2a"))     # Incorrect street type

    def test_validate_living_place_building_number(self):
        # Test cases for validate_living_place method - number of building should be exactly 2 symbols,
        # the first should be a digit, the second can be a digit or small letter
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 2a"))
        # Edge cases
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 2"))    # Building number too short
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 22aa"))  # Building number too long
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. a2"))    # Building number starts with a letter
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. aa"))    # Building number contains two letters
    
    def test_validate_index_length(self):
        # Test cases for validate_index method - index should be exactly 5 digits
        self.assertTrue(self.validator.validate_index("12345"))
        # Edge cases
        self.assertFalse(self.validator.validate_index("1234"))      # Too short
        self.assertFalse(self.validator.validate_index("123456"))    # Too long
        self.assertFalse(self.validator.validate_index("abcde"))     # Contains non-digit characters

    def test_validate_phone_format(self):
        # Test cases for validate_phone method - should be in the format "+380951234567" or "+38 (095) 123-45-67"
        self.assertTrue(self.validator.validate_phone("+380951234567"))
        self.assertTrue(self.validator.validate_phone("+38 (095) 123-45-67"))
        # Edge cases
        self.assertFalse(self.validator.validate_phone("380951234567"))          # Missing country code
        self.assertFalse(self.validator.validate_phone("+3801234567890"))       # Too many digits
        self.assertFalse(self.validator.validate_phone("+38 (095) 12345678"))   # Missing hyphens

    def test_validate_phone_length(self):
        # Test cases for validate_phone method - starts with "+" and has from 9 to 12 numbers
        self.assertTrue(self.validator.validate_phone("+380951234567"))
        self.assertTrue(self.validator.validate_phone("+38 (095) 123-45-67"))
        # Edge cases
        self.assertFalse(self.validator.validate_phone("+38"))                 # Too short
        self.assertFalse(self.validator.validate_phone("+380951234567890"))     # Too long
        self.assertFalse(self.validator.validate_phone("+38 (095) 12")) 

    def test_validate_email_format(self):
        # Test cases for validate_email method - should be in the format "username@domain.type"
        self.assertTrue(self.validator.validate_email("user@example.com"))
        self.assertTrue(self.validator.validate_email("someone@ucu.edu.ua"))
        # Edge cases
        self.assertFalse(self.validator.validate_email("user@.com"))           # Missing domain
        self.assertFalse(self.validator.validate_email("user@example"))        # Missing type
        self.assertFalse(self.validator.validate_email("@example.com"))         # Missing username
        self.assertFalse(self.validator.validate_email("user@domain"))          # Missing type
        self.assertFalse(self.validator.validate_email("user@domain."))         # Missing type
        self.assertFalse(self.validator.validate_email("user@@example.com"))    # Double "@" symbol
        self.assertFalse(self.validator.validate_email("user@domain@.com"))     # Double "@" symbol
        self.assertFalse(self.validator.validate_email("user@domain.com@"))     # Double "@" symbol
        self.assertFalse(self.validator.validate_email("user@example.com."))    # Extra dot in type
        self.assertFalse(self.validator.validate_email("user@domain@com"))     # Missing dot in type
        self.assertFalse(self.validator.validate_email("userrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr@domain@com"))     # Username too long

    def test_validate_email_username(self):
        # Test cases for validate_email method - username constraints
        self.assertTrue(self.validator.validate_email("user@example.com"))
        # Edge cases
        self.assertFalse(self.validator.validate_email(".user.example@domain.com"))  # Dot as first character
        self.assertFalse(self.validator.validate_email(".user@domain.com"))          # Dot as last character
        self.assertFalse(self.validator.validate_email("user..example@domain.com"))  # Consecutive dots
        self.assertFalse(self.validator.validate_email("user@domain.com"*20))        # Username too long
        self.assertFalse(self.validator.validate_email("user@domain.com_"))          # Underscore not allowed

    def test_validate_email_domain(self):
        # Test cases for validate_email method - domain constraints
        self.assertTrue(self.validator.validate_email("user@example.com"))
        # Edge cases
        self.assertFalse(self.validator.validate_email("user@example.com."))         # Extra dot at the end of domain
        self.assertFalse(self.validator.validate_email("user@Example.com"))          # Upper case letters in domain
        self.assertFalse(self.validator.validate_email("user@domain"*50))            # Domain too long
        self.assertFalse(self.validator.validate_email("user@domain.com-"))           # Hyphen not allowed

    def test_validate_email_type(self):
        # Test cases for validate_email method - type constraints
        self.assertTrue(self.validator.validate_email("user@example.com"))
        # Edge cases
        self.assertFalse(self.validator.validate_email("user@example.com1"))         # Invalid type
        self.assertFalse(self.validator.validate_email("user@example"))              # Missing type
        self.assertFalse(self.validator.validate_email("user@example.comm"))          # Type with more than 3 characters

    def test_validate_id_format(self):
        # Test cases for validate_id method - should be exactly 6 digits
        self.assertTrue(self.validator.validate_id("102345"))
        # Edge cases
        self.assertFalse(self.validator.validate_id("123456"))      # No zero
        self.assertFalse(self.validator.validate_id("1023045"))     # Multiple zeros
        self.assertFalse(self.validator.validate_id("abc000"))      # Contains non-digit characters
        self.assertFalse(self.validator.validate_id(""))            # Empty string

    def test_validate_id_one_zero(self):
        # Test cases for validate_id method - should contain exactly one zero
        self.assertTrue(self.validator.validate_id("102345"))
        self.assertTrue(self.validator.validate_id("120345"))
        self.assertTrue(self.validator.validate_id("123405"))
        self.assertTrue(self.validator.validate_id("123450"))
        # Edge cases
        self.assertFalse(self.validator.validate_id("100000"))     # All zeros
        self.assertFalse(self.validator.validate_id("000000")) 

    def test_validate_all_data(self):
        # Test cases for validate method
        valid_data = "John Doe,25,Ukraine,Lviv,Koselnytska st. 2a,12345,+380951234567,user@example.com,102345"
        invalid_data_short = "John Doe,25,Ukraine,Lviv,Koselnytska st. 2a,12345,+380951234567,user@example.com"  # Missing id
        invalid_data_long = "John Doe,25,Ukraine,Lviv,Koselnytska st. 2a,12345,+380951234567,user@example.com,102345,extra"  # Extra data

        self.assertTrue(self.validator.validate(valid_data))
        self.assertFalse(self.validator.validate(invalid_data_short))
        self.assertFalse(self.validator.validate(invalid_data_long))

    def test_validate_whitespace_separator(self):
        # Test cases for validate method - whitespace separator
        valid_data = "John Doe, 25, Ukraine, Lviv, Koselnytska st. 2a, 12345, +380951234567, user@example.com, 102345"
        self.assertTrue(self.validator.validate(valid_data))

    def test_validate_semicolon_separator(self):
        # Test cases for validate method - semicolon separator
        valid_data = "John Doe;25;Ukraine;Lviv;Koselnytska st. 2a;12345;+380951234567;user@example.com;102345"
        self.assertTrue(self.validator.validate(valid_data))

if __name__ == "__main__":
    unittest.main()
#when asked to optimize the test cases, the logic behind some of them was broken
#AI generated invalid tests
import unittest
from validator import Validator

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_name_surname(self):
        valid_cases = ["John Doe", "Alice Smith"]
        invalid_cases = ["John", "John Alex Doe", "john doe", "John doe", "JOhn DOe"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_name_surname(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_name_surname(case))

    def test_validate_name_surname_first_uppercase(self):
        valid_cases = ["John Doe", "Alice Smith"]
        invalid_cases = ["john doe", "John doe", "JOhn DOe"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_name_surname(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_name_surname(case))

    def test_validate_name_surname_size(self):
        valid_cases = ["John Doe", "Alice Smith"]
        invalid_cases = ["J", "A"*31, "JohnDoe"*10]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_name_surname(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_name_surname(case))

    def test_validate_name_surname_no_digits_punctuation(self):
        valid_cases = ["John Doe", "Alice Smith"]
        invalid_cases = ["John2 Doe", "Alice, Smith", "Joh@n Doe"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_name_surname(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_name_surname(case))

    def test_validate_age(self):
        valid_cases = ["25", "50", "16", "99"]
        invalid_cases = ["15", "100", "-5", "abc"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_age(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_age(case))

    def test_validate_country(self):
        valid_cases = ["Ukraine", "France"]
        invalid_cases = ["A"*10, "ukraine", "123Country", ""]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_country(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_country(case))

    def test_validate_region(self):
        valid_cases = ["Lviv123", "Kharkiv"]
        invalid_cases = ["A"*10, "123Region", ""]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_region(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_region(case))

    def test_validate_living_place_format(self):
        valid_cases = ["Koselnytska st. 2a"]
        invalid_cases = ["Koselnytska street 2a", "Koselnytska 2a"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_living_place(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_living_place(case))

    def test_validate_living_place_street_name(self):
        valid_cases = ["Koselnytska st. 2a"]
        invalid_cases = ["Main St. 2a", "Longest Street Ever St. 2a", "123 Street 2a", "street 2a"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_living_place(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_living_place(case))

    def test_validate_living_place_street_type(self):
        valid_cases = ["Koselnytska st. 2a"]
        invalid_cases = ["Koselnytska street 2a", "Koselnytska ave. 2a"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_living_place(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_living_place(case))

    def test_validate_living_place_building_number(self):
        valid_cases = ["Koselnytska st. 2a"]
        invalid_cases = ["Koselnytska st. 2", "Koselnytska st. 22aa", "Koselnytska st. a2", "Koselnytska st. aa"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_living_place(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_living_place(case))

    def test_validate_index_length(self):
        valid_cases = ["12345"]
        invalid_cases = ["1234", "123456", "abcde"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_index(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_index(case))

    def test_validate_phone_format(self):
        valid_cases = ["+380951234567", "+38 (095) 123-45-67"]
        invalid_cases = ["380951234567", "+3801234567890", "+38 (095) 12345678"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_phone(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_phone(case))

    def test_validate_phone_length(self):
        valid_cases = ["+380951234567", "+38 (095) 123-45-67"]
        invalid_cases = ["+38", "+380951234567890", "+38 (095) 12"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_phone(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_phone(case))

    def test_validate_email_format(self):
        valid_cases = ["user@example.com", "someone@ucu.edu.ua"]
        invalid_cases = ["user@.com", "user@example", "@example.com", "user@domain", "user@domain.", "user@@example.com", "user@domain@.com", "user@domain.com@", "user@example.com.", "user@domain@com", "userrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr@domain@com"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_email(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_email(case))

    def test_validate_email_username(self):
        valid_cases = ["user@example.com"]
        invalid_cases = [".user.example@domain.com", ".user@domain.com", "user..example@domain.com", "user@domain.com"*20, "user@domain.com_", ]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_email(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_email(case))

    def test_validate_email_domain(self):
        valid_cases = ["user@example.com"]
        invalid_cases = ["user@example.com.", "user@Example.com", "user@domain"*50, "user@domain.com-", ]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_email(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_email(case))

    def test_validate_email_type(self):
        valid_cases = ["user@example.com"]
        invalid_cases = ["user@example.com1", "user@example", "user@example.comm", ]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_email(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_email(case))

    def test_validate_id_format(self):
        valid_cases = ["102345"]
        invalid_cases = ["123456", "1023045", "abc000", ""]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_id(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_id(case))

    def test_validate_id_one_zero(self):
        valid_cases = ["102345", "120345", "123405", "123450"]
        invalid_cases = ["100000", "000000"]
        for case in valid_cases:
            self.assertTrue(self.validator.validate_id(case))
        for case in invalid_cases:
            self.assertFalse(self.validator.validate_id(case))

    def test_validate_all_data(self):
        valid_data = "John Doe,25,Ukraine,Lviv,Koselnytska st. 2a,12345,+380951234567,user@example.com,102345"
        invalid_data_short = "John Doe,25,Ukraine,Lviv,Koselnytska st. 2a,12345,+380951234567,user@example.com"  # Missing id
        invalid_data_long = "John Doe,25,Ukraine,Lviv,Koselnytska st. 2a,12345,+380951234567,user@example.com,102345,extra"  # Extra data
        self.assertTrue(self.validator.validate(valid_data))
        self.assertFalse(self.validator.validate(invalid_data_short))
        self.assertFalse(self.validator.validate(invalid_data_long))

    def test_validate_whitespace_separator(self):
        valid_data = "John Doe, 25, Ukraine, Lviv, Koselnytska st. 2a, 12345, +380951234567, user@example.com, 102345"
        self.assertTrue(self.validator.validate(valid_data))

    def test_validate_semicolon_separator(self):
        valid_data = "John Doe;25;Ukraine;Lviv;Koselnytska st. 2a;12345;+380951234567;user@example.com;102345"
        self.assertTrue(self.validator.validate(valid_data))

if __name__ == "__main__":
    unittest.main()

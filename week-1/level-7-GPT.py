#Рівень 7: https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
#Початковий розвʼязок ШІ
def validate_pin(pin):
    # Check if the pin contains only digits and its length is either 4 or 6
    return len(pin) in (4, 6) and pin.isdigit()

#При уточненні щодо використання бібліотеки re (regex):
#Chat GPT загалом непогано генерує регулярні вирази, але не враховує edge cases:
#(у цьому випадку - new line character у кінці рядка), тому код не цілком правильний

import re

def validate_pin(pin):
    # Define the regex pattern to match either 4 or 6 digits
    pattern = re.compile(r'^(\d{4}|\d{6})$')
    # Use the match method to check if the pin matches the pattern
    return bool(pattern.match(pin))

#Chat GPT генерує повністю правильний код, якщо надати йому конкретні приклади тестів, що не проходять
import re

def validate_pin(pin):
    # Define the regex pattern to match either 4 or 6 digits, with no leading or trailing spaces or newline characters
    pattern = re.compile(r'^\s*(\d{4}|\d{6})\s*$')
    # Use the match method to check if the pin matches the pattern
    return bool(pattern.match(pin)) and len(pin) == len(pin.strip())

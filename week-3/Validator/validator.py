#corrected code
#the problem was with the validation of email
"""validator"""
import re

class Validator:
    """Validator"""
    @staticmethod
    def validate_name_surname(name_surname: str):
        """validate name and surname"""
        return bool(re.match(r'^[A-Z][a-z]{1,29} [A-Z][a-z]{1,29}$', name_surname))
    @staticmethod
    def validate_age(age: str):
        """validate age"""
        return bool(re.match(r'^(1[6-9]|[2-9][0-9])$', age))
    @staticmethod
    def validate_country(country: str):
        """validate country"""
        return bool(re.match(r'^[A-Z][a-zA-Z]{1,9}$', country))
    @staticmethod
    def validate_region(region: str):
        """validate region"""
        return bool(re.match(r'^[A-Z][a-zA-Z1-9]{1,9}$', region))
    @staticmethod
    def validate_living_place(living_place: str):
        """validate living place"""
        if len(living_place.split(' '))==3:
            street, type_, number = living_place.split(' ')
        else:
            return False
        return bool(re.match(r'^[A-Z][a-zA-Z]{2,19}$', street)) \
and bool(re.match(r'^st.$|^av.$|^prosp.$|^rd.$', type_)) \
and bool(re.match(r'^[1-9][0-9a-z]$', number))
    @staticmethod
    def validate_index(index: str):
        """validate index"""
        return bool(re.match(r'^[0-9]{5}$', index))
    @staticmethod
    def validate_phone(phone: str):
        """validate phone"""
        return bool(re.match(r'^\+\d{9,12}$|^\+\d{2} \(\d{3}\) \d{3}-\d{2}-\d{2}', phone))
    @staticmethod
    def validate_email(email: str):
        """validate email"""
        return bool(re.match(r'^[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~]{1,64}(\.[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~]+)*@[a-z]{1,255}(\.[a-z]+)*\.(com|org|edu|gov|net|ua)$', \
email))
    @staticmethod
    def validate_id(id: str):
        """validate id"""
        return bool(re.match(r'^(?=(?:[^0]*0[^0]*){1}[^0]*$)\d{6}$', id))

    def validate(self, data: str):
        """general validation"""
        lst = data.replace(';', ',').replace(', ', ',').replace('; ', ',').split(',')
        if len(lst) < 9 or len(lst) > 9:
            return False
        return self.validate_name_surname(lst[0]) and \
self.validate_age(lst[1]) and self.validate_country(lst[2]) \
and self.validate_region(lst[3]) and self.validate_living_place(lst[4]) \
and self.validate_index(lst[5]) and self.validate_phone(lst[6]) and \
self.validate_email(lst[7]) and self.validate_id(lst[8])

"""
Write a python function to validate the regular expression for the following:-
a.)	Email Address
b.)	Mobile numbers of Bangladesh
c.)	Telephone numbers of USA
d.)	16 character Alpha-Numeric password composed of alphabets of Upper Case, Lower Case, Special Characters, Numbers.
"""

import re

#validation for email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

#validation for bangladesh mobile number
def validate_bangladesh_mobile(mobile_number):
    pattern = r'^(?:\+880|880)?[1-9][0-9]{9}$'
    if re.match(pattern, mobile_number):
        return True
    else:
        return False

#validation for US telephone number
def validate_usa_telephone(telephone_number):
    pattern = r'^(?:\+1\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    if re.match(pattern, telephone_number):
        return True
    else:
        return False

#validation for password
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    if re.match(pattern, password):
        return True
    else:
        return False
    
# Main program
print(validate_email('example@example.com')) 
print(validate_bangladesh_mobile('+8801712345678'))  
print(validate_usa_telephone('(123) 456-7890'))  
print(validate_password('A1b@cfghijklmnop')) 

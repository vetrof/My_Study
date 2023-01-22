# email validator
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

from validator_collection import validators, checkers, errors

email = input("What's your email address? ")

try:
    email_address = validators.email(email)
    # Will raise an EmptyValueError
except errors.EmptyValueError:
    print('EmptyValueError')
    # Handling logic goes here
except errors.InvalidEmailError:
    print('Invalid')
    # More handlign logic goes here
else:
    print('valid')
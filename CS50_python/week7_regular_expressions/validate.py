import re


email = input('you email:').strip()

if re.search(r"^\w+@\w+\.(com|ru)$", email, re.IGNORECASE):
    print('valid')

else:
    print('invalid')
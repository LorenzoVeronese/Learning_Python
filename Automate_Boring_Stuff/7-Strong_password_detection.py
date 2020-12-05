'''TEXT
Write a function that uses regular expressions to make sure the password string it is passed is strong. 
A strong password is defined as one that is at least eight characters long, contains both uppercase and 
lowercase characters, and has at least one digit. You may need to test the string against multiple regex 
patterns to validate its strength.'''

'''SOLUTION
---regex for uppercase [A-Z]
---regex for lowercase [a-z]
---regex for digit \d
---regex for 8 characters
'''

import re
regex_upperc=re.compile(r'[A-Z]{1}')
regex_lowerc=re.compile(r'[a-z]{1}')
regex_digit=re.compile (r'\d')
regex_eight=re.compile(r'.{8}')

test='Findaway6'

if regex_upperc.search(test)==None or regex_lowerc.search(test)==None or regex_digit.search(test)==None or regex_eight.search(test)==None:
    print('Your password isn\'t secure.')
else:
    print('Your password is secure.')

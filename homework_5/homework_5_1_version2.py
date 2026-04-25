#

my_str = input(f'Enter a string: ')
result = True
from string import digits, ascii_letters, punctuation, ascii_uppercase
from keyword import kwlist

# the string cannot start with a digit
if my_str[0] in digits:
    result = False
# the string must not be any of the registered words
elif my_str in kwlist:
    result = False
# the string cannot contain more one underscore
elif '__' in my_str:
    result = False
# the string cannot contain uppercase letters and spaces or punctuation marks, except for the underscore
else:
    punctuation_str = punctuation.replace('_', ' ')
    for i in my_str:
        if i in ascii_uppercase or i in punctuation_str:
            result = False
            break
print(result)
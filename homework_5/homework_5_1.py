
import string, keyword
my_str = input(f'Enter a string: ')

# the string cannot start with a digit
starts_with_non_digit = True
for i in string.digits:
    if my_str[0].startswith(f'{i}'):
        starts_with_non_digit = False
        #print(f'The string cannot start with a digit')
        break

# the string cannot contain uppercase letters
contains_no_uppercase = True
if starts_with_non_digit:
    k = 0
    while k < len(my_str):
        for j in string.ascii_uppercase:
            if my_str[k].startswith(f'{j}'):
                contains_no_uppercase = False
                #print(f'The string cannot contain uppercase letters')
                k = len(my_str)
                break
        k += 1

# the string cannot contain spaces or punctuation marks, except for the underscore
no_space_punct_allow_underscore = True
if starts_with_non_digit and contains_no_uppercase:
    l = 0
    punctuation_str = string.punctuation.replace('_', ' ')
    while l < len(my_str):
        for a in punctuation_str:
            if my_str[l].startswith(f'{a}'):
                no_space_punct_allow_underscore = False
                #print(f'The string cannot contain spaces or punctuation marks, except for the underscore')
                l = len(my_str)
                break
        l += 1

# the string must not be any of the registered words
not_in_registered_words = True
if starts_with_non_digit and contains_no_uppercase and no_space_punct_allow_underscore:
    for c in keyword.kwlist:
        if c in my_str and len(c) == len(my_str):
            not_in_registered_words = False
            #print(f'The string must not be any of the registered words')
            break

# the string cannot contain more one underscore
allow_only_one_underscore = True
if (starts_with_non_digit and contains_no_uppercase and no_space_punct_allow_underscore
        and not_in_registered_words):
    d = 0
    while d < len(my_str)-1:
        if '_' in my_str[d] and my_str[d+1].startswith('_'):
            allow_only_one_underscore = False
            #print(f'The string cannot contain more one underscore')
            d = len(my_str)
        d += 1

# result
if (starts_with_non_digit and contains_no_uppercase and no_space_punct_allow_underscore
        and not_in_registered_words and allow_only_one_underscore):
    print('True')
else:
    print('False')
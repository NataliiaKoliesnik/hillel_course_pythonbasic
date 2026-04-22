
my_str = input(f'Enter a string: ')
import string, keyword

# the string cannot start with a digit
result_1 = True
for i in string.digits:
    if my_str[0].startswith(f'{i}'):
        result_1 = False
        #print(f'The string cannot start with a digit')
        break

# the string cannot contain uppercase letters
result_2 = True
if result_1:
    k = 0
    while k < len(my_str):
        for j in string.ascii_uppercase:
            if my_str[k].startswith(f'{j}'):
                result_2 = False
                #print(f'The string cannot contain uppercase letters')
                k = len(my_str)
                break
        k += 1

# the string cannot contain spaces or punctuation marks, except for the underscore
result_3 = True
if result_1 and result_2:
    l = 0
    punctuation_str = string.punctuation.replace('_', ' ')
    while l < len(my_str):
        for a in punctuation_str:
            if my_str[l].startswith(f'{a}'):
                result_3 = False
                #print(f'The string cannot contain spaces or punctuation marks, except for the underscore')
                l = len(my_str)
                break
        l += 1

# the string must not be any of the registered words
result_4 = True
if result_1 and result_2 and result_3:
    for c in keyword.kwlist:
        if c in my_str and len(c) == len(my_str):
            result_4 = False
            #print(f'The string must not be any of the registered words')
            break

# the string cannot contain more one underscore
result_5 = True
if result_1 and result_2 and result_3 and result_4:
    d = 0
    while d < len(my_str)-1:
        if '_' in my_str[d] and my_str[d+1].startswith('_'):
            result_5 = False
            #print(f'The string cannot contain more one underscore')
            d = len(my_str)
        d += 1

# result
if result_1 and result_2 and result_3 and result_4 and result_5:
    print(f'True')
else:
    print(f'False')
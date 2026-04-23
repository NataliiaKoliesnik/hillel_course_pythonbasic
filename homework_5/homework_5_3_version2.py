# hashtag
my_str = input(f'Enter a string: ')
from string import  punctuation

# 3. each word starts with a capital letter
my_str = my_str.title()

# 1. no symbols or spaces
my_str_1 = str()
for i in my_str:
    if i not in punctuation and i not in ' ':
        my_str_1 += i

# adding a hashtag
my_str_1 = '#' + my_str_1

# 2. the length of the hashtag must not exceed 140 characters
if len(my_str_1) > 140:
    my_str_1 = my_str_1[:140]

print(f'{my_str_1}')

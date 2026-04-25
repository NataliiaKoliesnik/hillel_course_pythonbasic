# hashtag
my_str = input(f'Enter a string: ')
from string import  punctuation

# 3. each word starts with a capital letter
my_str = my_str.title()

# 1. no symbols or spaces
alnum_str = str()
for i in my_str:
    if i not in punctuation and not i.isspace():
        alnum_str += i

# adding a hashtag
alnum_str = f'#{alnum_str}'

# 2. the length of the hashtag must not exceed 140 characters
if len(alnum_str) > 140:
    my_str_1 = alnum_str[:140]

print(alnum_str)

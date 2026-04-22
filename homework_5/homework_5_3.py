# hashtag
my_str = input(f'Enter a string: ')
import string

# 3. each word starts with a capital letter
my_str = my_str.title()
#print(f'{my_str}')

# 1. no symbols or spaces
my_str_1 = str()
i = 0
k = 0
while i < len(my_str):
    for j in string.punctuation:
        if my_str[i] == j or my_str[i] == ' ':
            k += 1
    if k == 0:
        my_str_1 += my_str[i]
    k = 0
    i += 1
#print(f'{my_str_1}')

# adding a hashtag
my_str_1 = '#' + my_str_1
#print(f'{my_str_1}')

# 2. the length of the hashtag must not exceed 140 characters
if len(my_str_1) > 140:
    my_str_1 = my_str_1[:140]
print(f'{my_str_1}')
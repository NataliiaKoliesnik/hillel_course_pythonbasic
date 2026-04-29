# letter range: returns all characters between them inclusive
# no error checking is required; the minimum value is always less than or equal to the maximum

from string import ascii_letters

my_str = input(f'Enter two letters separated by a hyphen, without spaces: ')
# find the start and the end of the range to be output
start_result, end_result = ascii_letters.index(my_str[0]), ascii_letters.index(my_str[-1])
print(ascii_letters[start_result: end_result + 1])
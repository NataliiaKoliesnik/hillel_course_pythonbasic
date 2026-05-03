# letter range: returns all characters between them inclusive
# no error checking is required; the minimum value is always less than or equal to the maximum

from string import ascii_letters

my_str = input(f'Enter two letters separated by a hyphen, without spaces: ')

start_result = 0
end_result = 1
for i in ascii_letters:
    if my_str[0] == i:
        start_result = ascii_letters.index(i) # find the start of the range to be output
    if my_str[2] == i:
        end_result = ascii_letters.index(i) + 1 # find the end of the range to be output
        break
print(ascii_letters[start_result:end_result])


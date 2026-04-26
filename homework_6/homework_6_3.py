# the product of the digits of an integer until it becomes <= 9

from string import digits

num = input(f'Enter a number: ')

# checking whether a value is an integer, including negative numbers
flag_num = 0
for i in num[1:]:
    if num[0] == '-' or num[0] in digits: # does the string start with - or a digit
        if i not in digits: # are all other characters digits
            flag_num += 1
            break
    else:
        flag_num += 1
        break

result = int(num)

if flag_num == 0: # are we working with a number
    while abs(result) > 9: # check the condition <= 9
        if str(result)[0] == '-': # does the new number start with -
            product = -1
            for i in str(result)[1:]:
                product *= int(i)
        else:
            product = 1
            for i in str(result):
                product *= int(i)
        result = product
    print(result)
else:
    print('You entered a non-number')

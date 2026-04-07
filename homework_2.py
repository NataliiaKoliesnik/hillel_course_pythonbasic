# homework 2
import math

# 1. the square of a number
# option 1
number_1 = input('Enter a number: ')
result_square = int(number_1) ** 2
print('The square of a number: ', result_square,'\n')
# option 2
number_2 = input('Enter a number: ')
result1_square = math.pow(int(number_2),2)
print('The square of a number:', result1_square,'\n')

# 2. the average of three numbers
number_3, number_4, number_5 = map(int, input('Enter three numbers: ').split(","))
result2 = (number_3 + number_4 + number_5) / 3
print('The average of three numbers:', result2,'\n')

# 3. conversion of minutes into hours
numer_6 = input('Enter the number of minutes: ')
result3_1, result3_2 = divmod(int(numer_6), 60)
print(result3_1, 'hours', result3_2, 'minutes', '\n')
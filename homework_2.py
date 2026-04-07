# homework 2
import math

# 1. the square of a number
# option 1
number_1 = input('Enter a number: ')
result_square = int(number_1) ** 2
print('The square of a number: ', result_square,'\n')
# option 2
number_2 = input('Enter a number: ')
result_1_square = math.pow(int(number_2),2)
print('The square of a number:', result_1_square,'\n')

# 2. the average of three numbers
number_3, number_4, number_5 = map(int, input('Enter three numbers: ').split(","))
result_2 = (number_3 + number_4 + number_5) / 3
print('The average of three numbers:', result_2,'\n')

# 3. conversion of minutes into hours
numer_6 = input('Enter the number of minutes: ')
result_3_1, result_3_2 = divmod(int(numer_6), 60)
print(result_3_1, 'hours', result_3_2, 'minutes', '\n')

# 4. discount calculation
numer_7 = input('Enter the price: ')
numer_8 = input('Enter the discount: ')
result_4 = int(numer_7) - int(numer_7) * int(numer_8) / 100
print('Price after discount: ', result_4, '\n')
# homework 2
import math

# 1. the square of a number
# option 1
number_1 = input('Enter a number: ')
print(number_1)
result_square = int(number_1) ** 2
print(result_square)
# option 2
number_2 = input('Enter a number: ')
print(number_2)
result1_square = math.pow(int(number_2),2)
print(result1_square)

# 2. the average of three numbers
number_3, number_4, number_5 = map(int, input('Enter three numbers: ').split(","))
print(number_3, number_4, number_5)
result2 = (number_3 + number_4 + number_5) / 3
print(result2)
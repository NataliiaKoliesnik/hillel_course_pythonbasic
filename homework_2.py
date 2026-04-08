# homework 2

# 1. the square of a number
# option 1
number_1 = input('Enter a number: ')
result_square = int(number_1) ** 2
print('The square of a number: ', result_square,'\n')
# option 2
number_2 = input('Enter a number: ')
result_1_square = pow(int(number_2),2)
print('The square of a number:', result_1_square,'\n')

# 2. the average of three numbers
number_3, number_4, number_5 = map(int, input('Enter three numbers separated by commas: ').split(","))
result_2 = (number_3 + number_4 + number_5) / 3
print('The average of three numbers:', result_2,'\n')

# 3. conversion of minutes into hours
number_6 = input('Enter the number of minutes: ')
result_3_1, result_3_2 = divmod(int(number_6), 60)
print(result_3_1, 'hours', result_3_2, 'minutes', '\n')

# 4. discount calculation
price = input('Enter the price: ')
discount = input('Enter the discount: ')
result_4 = int(price) - int(price) * int(discount) / 100
print('Price after discount: ', result_4, '\n')

# 5. the last digit of a number
number_9 = input('Enter a number: ')
result_5 = int(number_9) % 10
print('the last digit: ', result_5, '\n')

# 6. perimeter of a rectangle
length = input('Enter the length: ')
width = input('Enter the width: ')
perimeter = 2 * (int(length) + int(width))
print('The perimeter: ', perimeter, '\n')
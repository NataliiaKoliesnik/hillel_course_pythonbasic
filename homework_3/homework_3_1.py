# homework 3.1

# the simplest calculator
from decimal import Decimal
number_1 = input('Enter a number 1: ')
number_2 = input('Enter a number 2: ')
math_operation = input('Enter the mathematical operation that is performed on numbers (+,-,*,/): ')
if math_operation == '+':
    result_1 = Decimal(number_1) + Decimal(number_2)
    print('The result is ', result_1)
elif math_operation == '-':
    result_2 = Decimal(number_1) - Decimal(number_2)
    print('The result is ', result_2)
elif math_operation == '*':
    result_3 = Decimal(number_1) * Decimal(number_2)
    print('The result is ', result_3)
elif math_operation == '/':
    if Decimal(number_2) != 0:
        result_4 = Decimal(number_1) / Decimal(number_2)
        print('The result is ', result_4)
    else:
        print('You can not divide by zero')
else:
    print('You entered an invalid mathematical operation')
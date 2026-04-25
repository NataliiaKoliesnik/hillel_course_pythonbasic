# modified calculator: works as long as the user wants

from decimal import Decimal
number_1 = input(f'Enter a number 1: ')
number_2 = input(f'Enter a number 2: ')
calc_consent = 'y'
while calc_consent == 'y' or calc_consent == 'yes':
    math_operation = input(f'Enter the mathematical operation that is performed on numbers (+,-,*,/): ')
    if math_operation == '+':
        result_1 = Decimal(number_1) + Decimal(number_2)
        print(f'The result is {result_1}')
    elif math_operation == '-':
        result_2 = Decimal(number_1) - Decimal(number_2)
        print(f'The result is {result_2}')
    elif math_operation == '*':
        result_3 = Decimal(number_1) * Decimal(number_2)
        print(f'The result is {result_3}')
    elif math_operation == '/':
        if Decimal(number_2) != 0:
            result_4 = Decimal(number_1) / Decimal(number_2)
            print(f'The result is {result_4}')
        else:
            print(f'You can not divide by zero')
    else:
        print(f'You entered an invalid mathematical operation')
    calc_consent = input(f'Do you want to calculate another number? ').lower()

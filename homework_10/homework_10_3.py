# function for checking whether a number is even

def is_even(digit: int) -> bool:
    return True if digit % 2 == 0 else False

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
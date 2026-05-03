# palindrome check function

from string import punctuation
def is_palindrome(text):
    text = text.lower() # converting letters to lowercase
    # a new string without punctuation marks and spaces
    without_punctuation = ''.join(i for i in text if i not in punctuation and not i.isspace())
    # palindrome check and output of the result
    return without_punctuation == without_punctuation[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
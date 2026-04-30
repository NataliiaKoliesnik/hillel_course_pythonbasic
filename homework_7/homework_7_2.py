# a function to modify a string so that it starts with a capital letter and ends with a period

def correct_sentence(text):
    if text[-1] != '.': # whether the string already ends with a period
        text = f'{text}.'
    text = f'{text[0].upper()}{text[1:]}' # starts with a capital letter
    return text

# function testing
assert correct_sentence('greetings, friends') == 'Greetings, friends.', 'Test1'
assert correct_sentence('hello') == 'Hello.', 'Test2'
assert correct_sentence('Greetings. Friends') == 'Greetings. Friends.', 'Test3'
assert correct_sentence('Greetings, friends.') == 'Greetings, friends.', 'Test4'
assert correct_sentence('greetings, friends.') == 'Greetings, friends.', 'Test5'
print('ОК')
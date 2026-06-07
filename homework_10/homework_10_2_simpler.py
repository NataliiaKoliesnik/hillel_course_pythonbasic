# function for finding the first word in a given string

def first_word(text: str) -> str:
    from string import punctuation
    # we exclude the apostrophe because it is part of the word and add a space
    punctuation_str = punctuation.replace('\'', ' ')
    for letter in text:
        if letter in punctuation_str:
            text = text.replace(letter, ' ')
    return text.split()[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
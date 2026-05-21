# function for finding the first word in a given string

def first_word(text:str) -> str:
    from string import ascii_letters, punctuation
    # we exclude the apostrophe because it is part of the word and add a space
    punctuation_str = punctuation.replace('\'', ' ')
    for i, letter in enumerate(text):
        if letter in ascii_letters: # we check whether there are letters in our string
            start = i
            break
    else:
        return 'There is no such word'
    # we output the word if there are more characters or words
    for j in range(start + 1, len(text)):
        if text[j] in punctuation_str:
            return text[start:j]
    # we output the word if it is the only one
    return text[start:]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
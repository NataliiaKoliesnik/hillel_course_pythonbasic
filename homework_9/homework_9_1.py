# a function that determines the popularity of certain words in a text

def popular_words (text: str, words: list[str]) -> dict[str, int]:
    """
    a function that determines the popularity of certain words in a text
    :param text: str datatype
    :param words: list[str] datatype
    :return: dict[str, int] datatype
    """
    new_text = text.lower().split() # we convert our text into a list of lowercase words
    # we store in a dictionary the checked word and the number of its occurrences in our text
    return {i :new_text.count(i) for i in words}
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
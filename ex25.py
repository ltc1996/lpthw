def break_words(stuff):
    """this function will break up words for ux"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words:"""
    return sorted(words)

def print_first_word(words):
    """print the first word after poping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """print the last word after poping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """take in a full sentnce and return the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last_word(sentence):
    """print the first and last words of the sentnce"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorted the words tne print the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

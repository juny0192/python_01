def print_upper_words(list_of_words, must_start_with):
    """Change all words in the list_of_words in Upper cased"""

    for words in list_of_words:
        for char in must_start_with:
            if words.startswith(char):
                print(words.upper())
                
        


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=['h', 'y'])

print_upper_words(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])
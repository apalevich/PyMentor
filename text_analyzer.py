#!/usr/bin/env python3

'''
Here is a few tools to analyze a text.
Full list of functions and their returns:

* count_words — returns integer of how many words (more than 1 character) is here
* count_sentences - returns integers of how many sentences is here
* words in russian - returns integers of russian words
* words in english - returns integers of english words
* numbers - returns integers of numbers in a text (1 digit or more)
* capital letters - returns integers of upper letters in a text

Every feature realized as an separate function.

So general usecase for them is to give it a piece of text as an argument
and it returns the counters as integer.
'''

text_for_test = """
Допустим, наша цель — выяснить людей, места и все что угодно, связанные друг с другом в наших    документах. Иными словами, нам нужно построить социальную сеть, выполнив серию    преобразований, как показано на рис. 9.4. Начнем конструирование графа с применения   класса EntityExtractor, созданного в главе 7.

Затем добавим преобразователи, один   из которых отыскивает        пары связанных сущностей, а второй преобразует эти пары в граф."""

# first, we create strings with alphabet

rus_low = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rus_big = rus_low.upper()
eng_low = 'abcdefghijklmnopqrstuvwxyz'
eng_big = eng_low.upper()

def count_words(text):
    """
    This function counts words in a text.
    Numbers and words less than 2 characters doesn't counts:

    >>> count_words('Please buy one cucumber & 3 apples')
    5
    """
    words = 0
    text_array = list(map(str, text.split()))

    for i in text_array:
        if i[0].isalpha() and len(i) > 1:
            words += 1

    return words

def count_sentences(text):
    """
    Counts sentences in a text and return it as integer.
    Sentence in this case is beginning with an upper letter
    and ends with '.', '!' or '?'. At least 1

    >>> count_sentences(text_for_test)
    4
    """
    sentences = 1

    text_array = list(map(str, text.split()))
    testing_lenght = range(1, len(text_array))
    ending_characters = ['.', '!', '?']

    for i in testing_lenght:
        current_word = text_array[i]
        previous_word = text_array[i-1]
        if current_word[0].isupper() and previous_word[-1] in ending_characters:
            sentences += 1

    return sentences

def count_russian_words(text):
    """
    Counts words in Russian by checking its first letter:

    >>> count_russian_words(text_for_test)
    57
    """
    text_array = list(map(str, text.split()))
    russians = 0

    for word in text_array:
        if word[0] in rus_big or word[0] in rus_low:
            russians += 1

    return russians

def count_english_letters(text):
    """
    Counts words in English by checking its first letter:

    >>> count_english_letters(text_for_test)
    1
    """
    text_array = list(map(str, text.split()))
    english = 0

    for word in text_array:
        if word[0] in eng_big or word[0] in eng_low:
            english += 1

    return english

def count_capital_letters(text):
    """
    Counts words with Capital letters:

    >>> count_capital_letters(text_for_test)
    6
    """
    capitals = 0
    for c in text:
        if c.isupper():
            capitals += 1

    return capitals


if __name__ == "__main__":

    import doctest
    doctest.testmod()

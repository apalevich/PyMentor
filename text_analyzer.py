#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Here is a few tools to analyze a text.
Full list of functions and their returns:

* count_words — returns integer of how many words (more than 1 character) is here
* count_sentences - returns integers of how many sentences is here
* count_words_by_language - returns integers of words belongs to any alphabet
* count_capital_letters - returns integers of upper letters in a text

Every feature realized as an separate function.

So general usecase for them is to give it a piece of text as an argument
and it returns the counters as integer.

"""
# Sample text for doctect
TEXT_FOR_TEST = """
Допустим, наша цель — выяснить людей, места и все что угодно, связанные друг с другом в наших    документах. Иными словами, нам нужно построить социальную сеть, выполнив серию    преобразований, как показано на рис. 9.4. Начнем конструирование графа с применения   класса EntityExtractor, созданного в главе 7.

Затем добавим преобразователи, один   из которых отыскивает        пары связанных сущностей, а второй преобразует эти пары в граф."""

# First, we create alphabets
RUS_LOW = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
RUS_BIG = rus_low.upper()
RUS_ALPHABET = rus_low + rus_big
ENG_LOW = 'abcdefghijklmnopqrstuvwxyz'
ENG_BIG = eng_low.upper()
ENG_ALPHABET = eng_low + eng_big

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

def count_words_by_language(text, alphabet = eng_alphabet):
    """
    Counts words in a language by checking its first letter.
    First argument must be a string with text, second is an dictionary (optional).

    Dictionary is just a string or list with alphabet.
    Pay attention to include in dictionary both lowcase and uppercase letters:

    >>> count_words_by_language(text_for_test, rus_alphabet)
    57

    If dict is not specified, english alphabet is used by default:

    >>> count_words_by_language(text_for_test)
    1

    """
    text_array = list(map(str, text.split()))
    counter = 0

    for word in text_array:
        if word[0] in alphabet:
            counter += 1

    return counter

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

def count_numbers(text):
    """
    Count numbers in a text:

    >>> count_numbers(text_for_test)
    2

    """
    text_array = list(map(str, text.split()))
    numbers = 0

    for i in text_array:
        if i[0].isdigit():
            numbers += 1

    return numbers

if __name__ == "__main__":
    # Launch doctect
    import doctest
    doctest.testmod()

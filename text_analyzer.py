#!/usr/bin/env python3

# Дан текст (точно в код скопировать, не исправлять):
#
text = """
Допустим, наша цель — выяснить людей, места и все что угодно, связанные друг с другом в наших    документах. Иными словами, нам нужно построить социальную сеть, выполнив серию    преобразований, как показано на рис. 9.4. Начнем конструирование графа с применения   класса EntityExtractor, созданного в главе 7.

Затем добавим преобразователи, один   из которых отыскивает        пары связанных сущностей, а второй преобразует эти пары в граф."""
# Нужно посчитать количество:
#
# слов в нём;
# предложений;
# слов на русском языке;
# слов на англ. языке;
# чисел
# заглавных букв

'''
Here is a few tools to analyze a text. Here is a full list of functions and their features:

* count_words — counting words (more than 1 character)
* count_sentences - c
* words in russian
* words in english
* numbers
* capital letters

Every point has a separate counter and while done the function returns them all.
In future, I looking forward to improve function's ability to choose
required counters and make it return only their values.

So general usecase for text_analyzer is to give it a piece of text as an argument
and it returns all the counters as variables and their integers:

>>> text = """
... Допустим, наша цель — выяснить людей, места и все что угодно, связанные друг с другом в наших    документах. Иными словами, нам нужно построить социальную сеть, выполнив серию    преобразований, как показано на рис. 9.4. Начнем конструирование графа с применения   класса EntityExtractor, созданного в главе 7.
...
...Затем добавим преобразователи, один   из которых отыскивает        пары связанных сущностей, а второй преобразует эти пары в граф."""

>>> text_analyzer(text)

'''

# first, we create variables using in some functions

rus_low = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rus_big = rus_low.upper()
eng_low = 'abcdefghijklmnopqrstuvwxyz'
eng_big = eng_low.upper()

text_array = list(map(str, text.split()))
ending_characters = ['.', '!', '?']

def count_words(text):
    '''
    Function counts words in a text.
    Numbers and words less than 2 characters doesn't counts:

    >>> count_words('Please buy one cucumber & 3 apples')
    5
    '''
    # count words
    words = 0
    for i in text_array:
        if i[0].isalpha() and len(i) > 1:
            words += 1
    return words

def count_sentences(text):
    '''
    description
    '''
    sentences = 0
    sentence_beginning = 0
    sentence_ending = 0

    for i in text_array:
        if i[0] in eng_big or i[0] in rus_big:
            sentence_beginning += 1

        elif i[-1] in ending_characters:
            sentence_ending += 1

        if sentence_beginning > 0 and sentence_ending > 0:
            sentence_beginning, sentence_ending = 0, 0
            sentences += 1
        print('{}, sentence_beginning: {}, sentence_ending: {}, total: {}'.format(i, sentence_beginning, sentence_ending, sentences))

    return sentences

    # for c in text:
    #     if c == '.':
    #         sentences += 1

    # TODO: придумать, как исключить подсчёт точек в сокращениях и числах

def temp(text):
    # count russian words
    russians = 0
    # for i in text_array:
    #     if i[0].isalpha() and i[0].encode() >= 0 and i[0].encode() >= 0:
    #         russians += 1
    # TODO: проверить метод unicode и номера кириллических символов в ней,
    # либо придумать иной способ

    # count english words
    english = 0
    # for i in text_array:
    #     if i[0].isalpha() and i[0].encode() > 0 and i[0].encode() <= 128:
    #         english += 1
    # TODO: проверить метод unicode и номера кириллических символов в ней,
    # либо придумать иной способ

    # count numbers
    numbers = 0
    for i in text_array:
        if i[0].isdigit():
            numbers += 1

    # count capital letters
    capitals = 0
    for c in text:
        if c.isupper():
            capitals += 1

    print('words: {}, sentences: {}, russians: {}, english: {}, numbers: {}, capitals: {}'.format(words, sentences, russians, english, numbers, capitals))

if __name__ == "__main__":

    text_array = list(map(str, text.split()))
    print(text_array)

    print(count_sentences(text))

    # import doctest
    # doctest.testmod()

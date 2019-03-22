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
Here is analyze tool for a text. It counts:

* words
* sentences
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

def text_analyzer(text):

    #let's convert text into list, it reveals useful in a some counters
    text_array = list(map(str, text.split()))

    # count words
    words = 0
    for i in text_array:
        if i[0].isalpha() and len(i) > 1:
            words += 1

    # count sentences
    sentences = 0
    for c in text:
        if c == '.':
            sentences += 1
    # fix cases when last sentence doesn't ends with a dot
    if text[-1] != '.':
        sentence += 1
    # TODO: придумать, как исключить подсчёт точек в сокращениях и числах

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

    text_analyzer(text)

    # import doctest
    # doctest.testmod()

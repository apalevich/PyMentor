#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from operator import itemgetter

def exclude_stopwords(path_to_text: str, stopwords_source: str = 'https://github.com/Alir3z4/stop-words/raw/bd8cc1434faeb3449735ed570a4a392ab5d35291/russian.txt'):
    """Returns text statistics after cleaning it from "black-listed" words.

    The function takes path to the text from local computer as a string on input

    >>> exclude_stopwords('./sample.txt')
    'и - 6 раз, ты - 3 раза, солнце - 2 раза, друг - 2 раза, на - 2 раза, сквозь - 2 раза, в - 2 раза, милый - 2 раза, мороз - 1 раз, день - 1 раз, чудесный - 1 раз, еще - 1 раз, дремлешь - 1 раз, прелестный - 1 раз, пора - 1 раз, красавица - 1 раз, проснись - 1 раз, открой - 1 раз, сомкнуты - 1 раз, негой - 1 раз, взоры - 1 раз, навстречу - 1 раз, северной - 1 раз, авроры - 1 раз, звездою - 1 раз, севера - 1 раз, явись - 1 раз, вечор - 1 раз, помнишь - 1 раз, вьюга - 1 раз, злилась - 1 раз, мутном - 1 раз, небе - 1 раз, мгла - 1 раз, носилась - 1 раз, луна - 1 раз, как - 1 раз, бледное - 1 раз, пятно - 1 раз, тучи - 1 раз, мрачные - 1 раз, желтела - 1 раз, печальная - 1 раз, сидела - 1 раз, а - 1 раз, нынче - 1 раз, погляди - 1 раз, окно - 1 раз, под - 1 раз, голубыми - 1 раз, небесами - 1 раз, великолепными - 1 раз, коврами - 1 раз, блестя - 1 раз, снег - 1 раз, лежит - 1 раз, прозрачный - 1 раз, лес - 1 раз, один - 1 раз, чернеет - 1 раз, ель - 1 раз, иней - 1 раз, зеленеет - 1 раз, речка - 1 раз, подо - 1 раз, льдом - 1 раз, блестит - 1 раз, вся - 1 раз, комната - 1 раз, янтарным - 1 раз, блеском - 1 раз, озарена - 1 раз, веселым - 1 раз, треском - 1 раз, трещит - 1 раз, затопленная - 1 раз, печь - 1 раз, приятно - 1 раз, думать - 1 раз, у - 1 раз, лежанки - 1 раз, но - 1 раз, знаешь - 1 раз, не - 1 раз, велеть - 1 раз, ли - 1 раз, санки - 1 раз, кобылку - 1 раз, бурую - 1 раз, запречь - 1 раз, скользя - 1 раз, по - 1 раз, утреннему - 1 раз, снегу - 1 раз, предадимся - 1 раз, бегу - 1 раз, нетерпеливого - 1 раз, коня - 1 раз, навестим - 1 раз, поля - 1 раз, пустые - 1 раз, леса - 1 раз, недавно - 1 раз, столь - 1 раз, густые - 1 раз, берег - 1 раз, для - 1 раз, меня - 1 раз'

     By default it use russian words for "black-list" from github repository.
     You can change it by argument stopwords_source:
     >>> exclude_stopwords('./sample.txt', stopwords_source = 'https://raw.githubusercontent.com/Alir3z4/stop-words/bd8cc1434faeb3449735ed570a4a392ab5d35291/english.txt')
     'и - 6 раз, ты - 3 раза, солнце - 2 раза, друг - 2 раза, на - 2 раза, сквозь - 2 раза, в - 2 раза, милый - 2 раза, мороз - 1 раз, день - 1 раз, чудесный - 1 раз, еще - 1 раз, дремлешь - 1 раз, прелестный - 1 раз, пора - 1 раз, красавица - 1 раз, проснись - 1 раз, открой - 1 раз, сомкнуты - 1 раз, негой - 1 раз, взоры - 1 раз, навстречу - 1 раз, северной - 1 раз, авроры - 1 раз, звездою - 1 раз, севера - 1 раз, явись - 1 раз, вечор - 1 раз, помнишь - 1 раз, вьюга - 1 раз, злилась - 1 раз, мутном - 1 раз, небе - 1 раз, мгла - 1 раз, носилась - 1 раз, луна - 1 раз, как - 1 раз, бледное - 1 раз, пятно - 1 раз, тучи - 1 раз, мрачные - 1 раз, желтела - 1 раз, печальная - 1 раз, сидела - 1 раз, а - 1 раз, нынче - 1 раз, погляди - 1 раз, окно - 1 раз, под - 1 раз, голубыми - 1 раз, небесами - 1 раз, великолепными - 1 раз, коврами - 1 раз, блестя - 1 раз, снег - 1 раз, лежит - 1 раз, прозрачный - 1 раз, лес - 1 раз, один - 1 раз, чернеет - 1 раз, ель - 1 раз, иней - 1 раз, зеленеет - 1 раз, речка - 1 раз, подо - 1 раз, льдом - 1 раз, блестит - 1 раз, вся - 1 раз, комната - 1 раз, янтарным - 1 раз, блеском - 1 раз, озарена - 1 раз, веселым - 1 раз, треском - 1 раз, трещит - 1 раз, затопленная - 1 раз, печь - 1 раз, приятно - 1 раз, думать - 1 раз, у - 1 раз, лежанки - 1 раз, но - 1 раз, знаешь - 1 раз, не - 1 раз, велеть - 1 раз, ли - 1 раз, санки - 1 раз, кобылку - 1 раз, бурую - 1 раз, запречь - 1 раз, скользя - 1 раз, по - 1 раз, утреннему - 1 раз, снегу - 1 раз, предадимся - 1 раз, бегу - 1 раз, нетерпеливого - 1 раз, коня - 1 раз, навестим - 1 раз, поля - 1 раз, пустые - 1 раз, леса - 1 раз, недавно - 1 раз, столь - 1 раз, густые - 1 раз, берег - 1 раз, для - 1 раз, меня - 1 раз'

    """
    # Get text from a file
    with open(path_to_text, 'r', encoding = 'utf-8') as original_text:
        text_string = original_text.read()
        text_list = text_string.lower().split()

    # Download stop-words
    stopwords_list = []
    with urlopen(stopwords_source) as stopwords:
        for line in stopwords:
            stopwords_list.append(line)

    # Finally exclude stopwords from original text
    cleaned_text = []
    for word in text_list:
        if not word in stopwords_list:
            cleaned_text.append(word)

    # Create dictionary and count words down to it
    stats = {}
    for element in cleaned_text:
        keyword = ''

        for char in element:
            if char.isalpha():
                keyword += char

        if not keyword.isalpha():
            pass
        elif keyword in stats.keys():
            stats[keyword] += 1
        else:
            stats[keyword] = 1

    # Three ways to sort items of the dictionary
    def get_value(x):
        return x[1]
    sorted_stats = sorted(stats.items(), key = get_value, reverse = True)
    # sorted_stats = sorted(stats.items(), key = lambda x: x[1], reverse = True)
    # sorted_stats = sorted(stats.items(), key = itemgetter(1), reverse = True)

    # Construct stats in human-readable format
    stats_string = ''
    for i in sorted_stats:
        if i[0].isalpha():
            form = 'раз'
            if str(i[1])[-1] in ['2', '3', '4']:
                form = 'раза'
            stats_string += '{} - {} {}, '.format(i[0], i[1], form)

    return stats_string[:-2]

if __name__ == "__main__":

    # Test cases from docstrings
    import doctest
    doctest.testmod()

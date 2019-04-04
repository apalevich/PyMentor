#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, collections

def counter(text):
    """
    Counter function is designed to count
    how many times every words is found in a text and
    return it in human-readable format as a string.

    You can use it with a string:
    >>> print(counter("We don't need no education, We don't need no thought control"))
    'we - 2 раз
    need - 2 раз
    no - 2 раз
    thought - 1 раз
    control - 1 раз'

    Path to file as a string supported too:
    >>> print(counter('./sample.txt/'))
    'и - 6 раз\\nты - 3 раз\\nдруг - 2 раз\\nна - 2 раз\\nсквозь - 2 раз\\nв - 2 раз\\nмороз - 1 раз\\nдень - 1 раз\\nеще - 1 раз\\nпрелестный - 1 раз\\nоткрой - 1 раз\\nсомкнуты - 1 раз\\nнегой - 1 раз\\nвзоры - 1 раз\\nнавстречу - 1 раз\\nсеверной - 1 раз\\nзвездою - 1 раз\\nсевера - 1 раз\\nвьюга - 1 раз\\nмутном - 1 раз\\nнебе - 1 раз\\nмгла - 1 раз\\nкак - 1 раз\\nбледное - 1 раз\\nтучи - 1 раз\\nмрачные - 1 раз\\nпечальная - 1 раз\\nсидела - 1 раз\\nа - 1 раз\\nпогляди - 1 раз\\nпод - 1 раз\\nголубыми - 1 раз\\nнебесами - 1 раз\\nвеликолепными - 1 раз\\nблестя - 1 раз\\nснег - 1 раз\\nпрозрачный - 1 раз\\nлес - 1 раз\\nодин - 1 раз\\nель - 1 раз\\nиней - 1 раз\\nречка - 1 раз\\nподо - 1 раз\\nльдом - 1 раз\\nвся - 1 раз\\nкомната - 1 раз\\nянтарным - 1 раз\\nблеском - 1 раз\\nвеселым - 1 раз\\nтреском - 1 раз\\nтрещит - 1 раз\\nзатопленная - 1 раз\\nприятно - 1 раз\\nдумать - 1 раз\\nу - 1 раз\\nно - 1 раз\\nне - 1 раз\\nвелеть - 1 раз\\nли - 1 раз\\nсанки - 1 раз\\nкобылку - 1 раз\\nбурую - 1 раз\\nскользя - 1 раз\\nпо - 1 раз\\nутреннему - 1 раз\\nпредадимся - 1 раз\\nбегу - 1 раз\\nнетерпеливого - 1 раз\\nконя - 1 раз\\nнавестим - 1 раз\\nполя - 1 раз\\nнедавно - 1 раз\\nстоль - 1 раз\\nмилый - 1 раз\\nдля - 1 раз\\n'
    """
    try:
        with open(text, 'r', encoding = 'utf-8') as original_text:
            text_string = original_text.read()
            text_list = text_string.lower().split()
    except FileNotFoundError:
        text_string = text
        text_list = text_string.lower().split()

    answer = ''

    c = collections.Counter(text_list).most_common()

    for i in list(c):
        if i[0].isalpha():
            answer += '{} - {} раз\\n'.format(i[0], i[1])

    return answer

if __name__ == '__main__':
    # print(counter('./sample1.txt'))
    import doctest
    doctest.testmod()

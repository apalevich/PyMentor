#!/usr/bin/env python3

import collections

def counter(text):
    """
    Counter function is designed to count
    how many times every words is found in a text and
    return it in human-readable format as a string.

    You can use it with a string:
    >>> counter("We don't need no education, We don't need no thought control")
    'we - 2 раз, need - 2 раз, no - 2 раз, thought - 1 раз, control - 1 раз'

    Path to file as a string supported too:
    >>> counter('./sample.txt')
    'и - 6 раз, ты - 3 раз, друг - 2 раз, на - 2 раз, сквозь - 2 раз, в - 2 раз, мороз - 1 раз, день - 1 раз, еще - 1 раз, прелестный - 1 раз, открой - 1 раз, сомкнуты - 1 раз, негой - 1 раз, взоры - 1 раз, навстречу - 1 раз, северной - 1 раз, звездою - 1 раз, севера - 1 раз, вьюга - 1 раз, мутном - 1 раз, небе - 1 раз, мгла - 1 раз, как - 1 раз, бледное - 1 раз, тучи - 1 раз, мрачные - 1 раз, печальная - 1 раз, сидела - 1 раз, а - 1 раз, погляди - 1 раз, под - 1 раз, голубыми - 1 раз, небесами - 1 раз, великолепными - 1 раз, блестя - 1 раз, снег - 1 раз, прозрачный - 1 раз, лес - 1 раз, один - 1 раз, ель - 1 раз, иней - 1 раз, речка - 1 раз, подо - 1 раз, льдом - 1 раз, вся - 1 раз, комната - 1 раз, янтарным - 1 раз, блеском - 1 раз, веселым - 1 раз, треском - 1 раз, трещит - 1 раз, затопленная - 1 раз, приятно - 1 раз, думать - 1 раз, у - 1 раз, но - 1 раз, не - 1 раз, велеть - 1 раз, ли - 1 раз, санки - 1 раз, кобылку - 1 раз, бурую - 1 раз, скользя - 1 раз, по - 1 раз, утреннему - 1 раз, предадимся - 1 раз, бегу - 1 раз, нетерпеливого - 1 раз, коня - 1 раз, навестим - 1 раз, поля - 1 раз, недавно - 1 раз, столь - 1 раз, милый - 1 раз, для - 1 раз'
    """

    # Get original text from a file or string
    try:
        with open(text, 'r', encoding = 'utf-8') as original_text:
            text_string = original_text.read()
            text_list = text_string.lower().split()
    except FileNotFoundError:
        text_string = text
        text_list = text_string.lower().split()

    # Prepare string for function's result
    answer = ''

    # Sort words by quantity
    c = collections.Counter(text_list).most_common()

    # Add sorted words to result string in a human-readable format
    for i in list(c):
        if i[0].isalpha():
            form = 'раз'
            if i[1][-1] == ['2', '3', '4']:
                form = 'раза'
            answer += '{} - {} {}, '.format(i[0], i[1], form)

    # remove comma at ending
    while not answer[-1].isalpha():
        answer = answer[:-1]

    return answer

if __name__ == '__main__':

    import doctest
    doctest.testmod()

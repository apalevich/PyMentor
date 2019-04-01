#!/usr/bin/env python3

# TODO: написать доктест

from urllib.request import urlopen

def exclude_stopwords(path_to_text):
    # TODO: написать доктест

    # get input text from a file to list
    with open(path_to_text, 'r') as original_text:
        text_string = original_text.read()
        text_list = text_string.split()

    # download file with stop-words
    stopwords_source = 'https://github.com/Alir3z4/stop-words/raw/bd8cc1434faeb3449735ed570a4a392ab5d35291/russian.txt'
    stopwords_list = []
    with urlopen(stopwords_source) as stopwords:
        for line in stopwords:
            stopwords_list.append(line)

    # finally exclude stopwords from original text
    cleaned_text = []
    for word in text_list:
        if not word in stopwords_list:
            cleaned_text.append(word)

    #collect_statistics
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

    sorted_stats = sorted(stats.items(), key = lambda x: x[1], reverse = True)

    stats_string = ""

    for i in sorted_stats:
        stats_string += '{} — {} раз\n'.format(i[0], i[1])

    return stats_string

if __name__ == "__main__":
    print(exclude_stopwords('./sample.txt'))

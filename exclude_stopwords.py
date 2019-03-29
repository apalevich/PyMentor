#!/usr/bin/env python3

# TODO: написать доктест

import requests

def exclude_stopwords(path_to_text):
    # TODO: написать доктест

    # get input text from a file to list
    original_text = open(path_to_text, 'r')
    text_string = original_text.read()
    text_list = text_string.split()

    # download file with stop-words
    url = 'https://github.com/Alir3z4/stop-words/raw/bd8cc1434faeb3449735ed570a4a392ab5d35291/russian.txt'
    response = requests.get(url)
    stopwords = open('/tmp/stopwords.txt', 'wb')
    stopwords.write(response.content)
    stopwords.close()

    # make a list with stopwords
    stopwords_list = []
    stopwords = open('/tmp/stopwords.txt', 'r')
    for line in stopwords:
        stopwords_list.append(line[:-1])

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

        if keyword in stats.keys():
            stats[keyword] += 1
        else:
            stats[keyword] = 1

    return stats


# TODO:
# слова в виде листа
# считать сколько раз входит

if __name__ == "__main__":
    print(exclude_stopwords('/tmp/copy.txt'))

# TODO: выдавать статистику по частоте вхождения в текст каждого слова - самые частые слова сначала.

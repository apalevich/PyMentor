# get input text from a file
text = open('/tmp/text.txt', 'w')

# download file with stop-words
import requests
url = 'https://github.com/Alir3z4/stop-words/raw/bd8cc1434faeb3449735ed570a4a392ab5d35291/russian.txt'
response = requests.get(url)
stopwords = open('/tmp/stopwords.txt', 'wb')
stopwords.write(response.content)
stopwords.close()

#make a list with stopwords
sw = []
stopwords = open('/tmp/stopwords.txt', 'r')
for line in stopwords:
    sw.append(line[:-1])

# Удалить из текста stop_words, что бы они не участвовали в статистике.
text_set = list(map(str, text.split()))
stopwords_set = set(map(str, text.split()))
clear_text = text_set - stopwords_set

# выдавать статистику по частоте вхождения в текст каждого слова - самые частые слова сначала.

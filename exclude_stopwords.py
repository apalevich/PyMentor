# download file with stop-words
url = 'https://github.com/Alir3z4/stop-words/raw/bd8cc1434faeb3449735ed570a4a392ab5d35291/russian.txt'
response = requests.get(url)
stopwords = open('stopwords.txt', 'wb').write(r.content)
stopwords.close()

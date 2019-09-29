# word_cloud.py

stopwords = []
stopwords_file = open('word_cloud/stopwords', encoding='utf8')

for word in stopwords_file:
  stopwords.append(word.strip("\n"))

stopwords_file.close()
print(stopwords)

path = 'word_cloud/98-0.txt'
words_count = {}

file = open(path, encoding='utf8')
for word in file.read().lower().split():

      word = word.replace(".","")
      word = word.replace(",","")
      word = word.replace("\"","")
      word = word.replace("“","")

      if word in stopwords:
        continue
      if word in words_count:
        words_count[word] += 1
      else:
        words_count[word] = 1

sort = sorted(words_count, key=lambda word:words_count[word], reverse=True)[0:10]
# print(sort)
for word in sort:
 print(word, words_count[word])

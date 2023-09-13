import nltk

f = open ("tyger.txt", "r", encoding="utf8")
data = f.read()
tokens = nltk.word_tokenize(data)
tags = nltk.pos_tag(tokens)
print(tags)

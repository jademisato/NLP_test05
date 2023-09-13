import nltk
f = open ("tyger.txt", "r",)
data = f.read()
tokens = nltk.word_tokenize(data)
print(tokens)

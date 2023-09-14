import nltk

# Show tags for all words (全ての単語のタグを表示する)
f = open ("tyger.txt", "r", encoding="utf8")
data = f.read()
tokens = nltk.word_tokenize(data)
tags = nltk.pos_tag(tokens)

# Extract words with NNP tags (NNPタグを持つ単語を抽出する)
text_word = [word for word, pos in tags if pos == 'NNP']
print(text_word)
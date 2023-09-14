import nltk
import datetime

# Show tags for all words
# (全ての単語のタグを表示する)
f = open ("tyger.txt", "r", encoding="utf8")
data = f.read()
tokens = nltk.word_tokenize(data)
tags = nltk.pos_tag(tokens)
# print(tags)

# Extract words with NNP tags
# (NNPタグを持つ単語を抽出する)
text_word = [word for word, pos in tags if pos == 'NNP']

# Output words with NNP tags to the console
# (NNPタグを持つ単語をコンソールに出力する)
print("These contain NNP tags", text_word)

# Prepare the current date and time as a string for the file name
# (ファイル名用に現在日時を文字列で用意する)
file_datetime = datetime.datetime.now()
file_datetime_str = file_datetime.strftime('%Y%m%d_%H%M%S')

# Writing the extraction results to a file
# (抽出結果をファイルに書き込む)
with open(f'./result_{file_datetime_str}.txt', 'w', encoding="utf8") as f:
    for i in text_word:
        f.write(i + '\n')

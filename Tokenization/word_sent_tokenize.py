import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello there! Welcome to NLP. Let's learn together."

print("Word Tokenize:", word_tokenize(text))
print("Sentence Tokenize:", sent_tokenize(text))

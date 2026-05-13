import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

text = "Artificial Intelligence is changing the world"

# Tokenization
words = word_tokenize(text)
print("Tokens:", words)

# Word Frequency
print("Frequency:", Counter(words))

# Stop Words Removal
stop = stopwords.words('english')
filtered = [w for w in words if w.lower() not in stop]
print("After Stop Words Removal:", filtered)

# POS Tagging
print("POS Tagging:", nltk.pos_tag(words))

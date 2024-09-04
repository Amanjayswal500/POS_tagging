import nltk
from nltk import word_tokenize
from nltk import pos_tag

# Download necessary resources from nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define the sentence
sentence = "NLTK is a leading platform for building Python programs to work with human language data."

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Perform POS tagging
pos_tags = pos_tag(words)

# Print the sentence with its POS tags
for word, tag in pos_tags:
    print(f"{word}: {tag}")

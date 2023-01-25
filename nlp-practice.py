import nltk
from nltk import word_tokenize
text = word_tokenize("I am the cutest koogler in the world")
output = nltk.pos_tag(text)
print(output)
import nltk
from nltk.corpus import gutenberg

#download the dataset
try:
	text3 = gutenberg.words('bible-kjv.txt')
except LookupError:
	nltk.download("gutenberg")
	text3 = gutenberg.words('bible-kjv.txt')

def lexical_diversity(text):
	"""Calculate the lexical diversity of given text."""
	return len(set(text)) / len(text)

#Lets calculate the lexical diversity for text3
diversity_score = lexical_diversity(text3)
print(f"Lexical diversity of Bible: {diversity_score:.4f}")

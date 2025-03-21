import nltk
from nltk.corpus import gutenberg, stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer


try:
    nltk.data.find('corpora/wordnet.zip')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('corpora/stopwords.zip')
except LookupError:
    nltk.download("stopwords")

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def clean_text(words):
    """Removes punctuation and stopwords from a list of words."""
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalpha()]  
    words = [word for word in words if word not in stop_words] 
    return words

def apply_stemming(text):
    """Applies stemming to the text."""
    cleaned_words = clean_text(text)
    return [stemmer.stem(word) for word in cleaned_words]

def apply_lemmatization(text):
    """Applies lemmatization to the text."""
    cleaned_words = clean_text(text)
    return [lemmatizer.lemmatize(word) for word in cleaned_words]


sample_text = gutenberg.words('shakespeare-hamlet.txt')[:500]  # Using first 500 words


stemmed_words = apply_stemming(sample_text)
print("\nStemmed Words (First 50):")
print(stemmed_words[:50])


lemmatized_words = apply_lemmatization(sample_text)
print("\nLemmatized Words (First 50):")
print(lemmatized_words[:50])

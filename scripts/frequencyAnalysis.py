import nltk
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import gutenberg, stopwords


try:
    nltk.data.find('corpora/stopwords.zip')
except LookupError:
    nltk.download("stopwords")

def clean_text(words):
    """Removes punctuation and stopwords from a list of words."""
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalpha()] 
    words = [word for word in words if word not in stop_words]  
    return words

def word_frequency(text, num_words=20):
    """Finds the most common words in a cleaned text."""
    cleaned_words = clean_text(text)
    word_counts = Counter(cleaned_words)
    return word_counts.most_common(num_words)


texts = {
    "Bible (Genesis)": "bible-kjv.txt",
    "Moby Dick": "melville-moby_dick.txt",
    "Hamlet": "shakespeare-hamlet.txt"
}


for name, filename in texts.items():
    words = gutenberg.words(filename)
    common_words = word_frequency(words)
    print(f"\nTop 20 Words in {name}:")
    for word, count in common_words:
        print(f"{word}: {count}")

    
    plt.figure(figsize=(10, 5))
    words, counts = zip(*common_words)
    plt.bar(words, counts, color='blue')
    plt.xticks(rotation=45)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title(f"Top 20 Most Common Words in {name}")
    plt.show()
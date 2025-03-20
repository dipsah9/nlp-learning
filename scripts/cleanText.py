import nltk
import string
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

def lexical_diversity(text):
    """Calculates lexical diversity of cleaned text."""
    cleaned_words = clean_text(text)
    return len(set(cleaned_words)) / len(cleaned_words)


texts = {
    "Bible (Genesis)": "bible-kjv.txt",
    "Moby Dick": "melville-moby_dick.txt",
    "Hamlet": "shakespeare-hamlet.txt"
}

# Compute lexical diversity for each text
results = {}
for name, filename in texts.items():
    words = gutenberg.words(filename)
    diversity_score = lexical_diversity(words)
    results[name] = diversity_score
    print(f"Lexical Diversity (cleaned) of {name}: {diversity_score:.4f}")

# Sort results by lexical diversity
sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

# Display sorted results
print("\n--- Sorted Lexical Diversity Scores (Cleaned) ---")
for name, score in sorted_results:
    print(f"{name}: {score:.4f}")
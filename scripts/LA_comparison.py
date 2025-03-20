import nltk
from nltk.corpus import gutenberg


nltk.data.path.append('/Users/dipendrasah/nltk_data')

# Ensure dataset is downloaded only if missing
try:
    nltk.data.find('corpora/gutenberg.zip')
except LookupError:
    nltk.download("gutenberg", download_dir="/Users/dipendrasah/nltk_data")

def lexical_diversity(text):
    """Calculates the lexical diversity of a given text."""
    return len(set(text)) / len(text)

# Select texts for comparison
texts = {
    "Bible (Genesis)": "bible-kjv.txt",
    "Moby Dick": "melville-moby_dick.txt",
    "Hamlet": "shakespeare-hamlet.txt",
}

# Compute lexical diversity for each text
results = {}
for name, filename in texts.items():
    words = gutenberg.words(filename)
    diversity_score = lexical_diversity(words)
    results[name] = diversity_score
    print(f"Lexical Diversity of {name}: {diversity_score:.4f}")


sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)


print("\n--- Sorted Lexical Diversity Scores ---")
for name, score in sorted_results:
    print(f"{name}: {score:.4f}")
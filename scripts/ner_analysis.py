import spacy
from nltk.corpus import gutenberg

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Use the first 1000 words of Hamlet for demo
hamlet_text = " ".join(gutenberg.words("shakespeare-hamlet.txt")[:1000])

# Process the text
doc = nlp(hamlet_text)

print("Named Entities:\n")
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")
import spacy

# load small English model
nlp = spacy.load("en_core_web_sm")

text = "Hello there! Welcome to NLP. Let's learn together."
doc = nlp(text)

print("spaCy tokens:", [token.text for token in doc])
print("POS tags:", [(token.text, token.pos_) for token in doc])

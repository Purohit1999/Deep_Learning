import streamlit as st
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# one-time downloads (quiet)
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

st.title("Tokenizer Demo")

text = st.text_area(
    "Enter text:",
    "This is a simple example. It shows how the stopword filter works!",
    height=140
)

def remove_stopwords_from_text(txt: str):
    """Return original tokens, cleaned tokens, and number removed."""
    tokens = word_tokenize(txt)
    # keep only tokens with letters/numbers (skip pure punctuation)
    tokens = [t for t in tokens if any(ch.isalnum() for ch in t)]
    sw = set(stopwords.words("english"))
    cleaned = [t for t in tokens if t.lower() not in sw]
    removed_count = len(tokens) - len(cleaned)
    return tokens, cleaned, removed_count

if st.button("Tokenize & Remove Stopwords"):
    txt = text.strip()
    if not txt:
        st.warning("Please enter some text.")
    else:
        # (Task 1) sentence tokens + count (optional to keep)
        sentences = sent_tokenize(txt)
        st.write("Sentence tokens:", sentences)
        st.metric("Number of sentences", len(sentences))

        # (Task 2) stopword cleaning
        original, cleaned, removed_count = remove_stopwords_from_text(txt)
        st.subheader("Original word tokens")
        st.write(original)

        st.subheader("Cleaned tokens (stopwords removed)")
        st.write(cleaned)

        st.metric("Count of removed stopwords", removed_count)

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# one-time downloads (quiet)
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

st.title("Project 5 – Remove English Stopwords")

text = st.text_area(
    "Enter text:",
    "This is a simple example showing how the stopword filter works."
)

# Optional: keep negations (useful for sentiment tasks)
keep_neg = st.checkbox("Keep negations (no, not, nor, n't)", value=True)

if st.button("Clean text"):
    txt = text.strip()
    if not txt:
        st.warning("Please enter some text.")
    else:
        # tokenize and drop pure punctuation tokens
        tokens = [t for t in word_tokenize(txt) if any(ch.isalnum() for ch in t)]

        # build stopword set
        sw = set(stopwords.words("english"))
        if keep_neg:
            sw -= {"no", "not", "nor", "n't"}

        # lowercase for comparison
        cleaned = [t for t in tokens if t.lower() not in sw]
        removed = [t for t in tokens if t.lower() in sw]

        st.subheader("Cleaned tokens")
        st.write(cleaned)

        st.metric("Count of removed stopwords", len(removed))
        if removed:
            st.caption(f"Removed stopwords: {removed}")

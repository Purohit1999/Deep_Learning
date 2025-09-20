import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import pandas as pd

# one-time download for tokenizer
nltk.download("punkt", quiet=True)

st.title("Project 6 – Top 5 Most Common Words")
st.caption("Punctuation is excluded; words are lowercased.")

text = st.text_area(
    "Enter text:",
    "Hello hello! This is a simple demo. This demo shows a bar chart of common words."
)

TOP_K = 5  # required by task

def tokenize_without_punct(s: str):
    # keep tokens that contain at least one letter/number (drop pure punctuation)
    return [t.lower() for t in word_tokenize(s) if any(ch.isalnum() for ch in t)]

if st.button("Show Top 5"):
    txt = text.strip()
    if not txt:
        st.warning("Please enter some text.")
    else:
        tokens = tokenize_without_punct(txt)
        if not tokens:
            st.info("No word tokens found.")
        else:
            counts = Counter(tokens)
            top = counts.most_common(TOP_K)

            st.subheader("Tokens")
            st.write(tokens)

            st.subheader(f"Top {TOP_K} words")
            st.write(top)

            # bar chart: index = words
            df = pd.DataFrame(top, columns=["word", "count"]).set_index("word")
            st.bar_chart(df)

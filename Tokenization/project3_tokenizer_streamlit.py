# project3_tokenizer_streamlit.py
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import pandas as pd

# make sure punkt is available for tokenization
nltk.download("punkt", quiet=True)

st.title("Top 5 Most Common Words (Bar Chart)")
st.write("Punctuation is excluded. Words are lowercased; stopwords are **not** removed.")

text = st.text_area(
    "Enter text:",
    "Hello hello! This is a simple demo. This demo shows a bar chart of common words.",
    height=150
)

TOP_K = 5

def tokenize_no_punct(txt: str):
    # keep tokens that contain at least one letter/number (drop pure punctuation)
    tokens = [t.lower() for t in word_tokenize(txt) if any(ch.isalnum() for ch in t)]
    return tokens

if st.button("Show Top Words"):
    txt = text.strip()
    if not txt:
        st.warning("Please enter some text.")
    else:
        tokens = tokenize_no_punct(txt)
        st.write("Tokens (punctuation removed):", tokens)

        counts = Counter(tokens)
        if not counts:
            st.info("No word tokens found.")
        else:
            top = counts.most_common(TOP_K)
            st.subheader(f"Top {TOP_K} words")
            st.write(top)

            # Prep dataframe for bar chart (index must be the x-axis labels)
            df = pd.DataFrame(top, columns=["word", "count"]).set_index("word")
            st.bar_chart(df)

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# make sure punkt is available
nltk.download("punkt", quiet=True)

st.title("Tokenizer Demo")

text = st.text_area(
    "Enter text:",
    "Hello there! Welcome to NLP. Let's learn together.",
    height=150
)

if st.button("Tokenize"):
    txt = text.strip()
    if not txt:
        st.warning("Please enter some text.")
    else:
        # 1) Sentence tokenization
        sentences = [s.strip() for s in sent_tokenize(txt)]
        st.subheader("Sentence tokens")
        for i, s in enumerate(sentences, 1):
            st.write(f"{i}. {s}")

        # 2) Display number of sentences
        st.metric("Number of sentences", len(sentences))

        # 3) First and last word of input
        #    (filter out pure punctuation so first/last are real words)
        words_all = word_tokenize(txt)
        words = [w for w in words_all if any(ch.isalnum() for ch in w)]

        st.subheader("Word tokens")
        st.write(words)

        if words:
            st.success(f"First word: **{words[0]}**   |   Last word: **{words[-1]}**")
        else:
            st.info("No word tokens found.")

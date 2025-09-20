import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("punkt", quiet=True)

st.title("Sentence Tokenizer – Task 1")

text = st.text_area(
    "Enter your text:",
    "Hello there! Welcome to NLP. Let's learn together."
)

if st.button("Tokenize"):
    txt = text.strip()
    if not txt:
        st.warning("Please enter some text.")
    else:
        # 1) Tokenize at sentence level
        sentences = sent_tokenize(txt)
        st.subheader("Sentences")
        for i, s in enumerate(sentences, 1):
            st.write(f"{i}. {s}")

        # 2) Display number of sentences
        st.metric("Number of sentences", len(sentences))

        # 3) Display first and last word of user input
        #    (ignore pure punctuation so you get real words)
        words_all = word_tokenize(txt)
        words = [w for w in words_all if any(ch.isalnum() for ch in w)]
        st.subheader("Words")
        st.write(words)

        if words:
            st.success(f"First word: **{words[0]}**   |   Last word: **{words[-1]}**")
        else:
            st.info("No word tokens found.")

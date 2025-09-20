import streamlit as st
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import spacy

nltk.download("punkt")
nlp = spacy.load("en_core_web_sm")

st.title("NLP Tokenizer Demo")

text = st.text_area("Enter some text:", "Hello there! Welcome to NLP.")

if st.button("Tokenize"):
    st.subheader("Word Tokenization (NLTK)")
    st.write(word_tokenize(text))

    st.subheader("Sentence Tokenization (NLTK)")
    st.write(sent_tokenize(text))

    st.subheader("spaCy Tokens + POS Tags")
    doc = nlp(text)
    st.write([(token.text, token.pos_) for token in doc])

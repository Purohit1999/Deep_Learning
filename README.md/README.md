
---

# NLP\_1 – Tokenization & Text Cleaning (Streamlit + NLTK + spaCy)

Small, focused projects to learn core NLP preprocessing:

* sentence/word tokenization
* stopword removal
* punctuation/number cleaning
* top-word frequency charts
* quick spaCy POS/NER demo

## Folder structure

```
Tokenization/
  project1_tokenizer_streamlit.py        # Sentence tokenizer + count + first/last word
  project2_tokenizer_streamlit.py        # Streamlit tokenizer demo (task 2 baseline)
  project3_tokenizer_streamlit.py        # Top-5 most common words (bar chart)
  project4_tokenizer_streamlit.py        # Sentence tokenizer variant (saved by you as Project 4)
  project5_stopwords_streamlit.py        # Remove English stopwords (+ keep-negations option)
  project6_top_words_streamlit.py        # Top-5 words bar chart (punctuation removed)
  project_tokenizer_streamlit.py         # General tokenizer playground
  word_sent_tokenize.py                  # NLTK word/sentence tokenize (script)
  using_split.py                         # Naive .split() examples
  spacy_tokenizer.py                     # spaCy tokens + POS + entities
  Removing_p_n.py                        # Remove punctuation & numbers
  text_cleaning_demo.py                  # Lowercase, regex clean, stopwords pipeline
requirements.txt
```

## Quick start (Windows + PowerShell)

```powershell
cd "C:\Users\puroh\Downloads\NLP\NLP_1"

# 1) Create/activate venv (first time)
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

# 2) Install deps
pip install -r requirements.txt

# 3) One-time model downloads
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
python -m spacy download en_core_web_sm
```

> If Anaconda “(base)” auto-activates, use a regular PowerShell or explicitly run:
> `& .\.venv\Scripts\python.exe ...`

## How to run (Streamlit apps)

```powershell
# Project 1 – sentences, count, first/last word
python -m streamlit run .\Tokenization\project1_tokenizer_streamlit.py

# Project 2 – tokenizer demo (task 2 baseline UI)
python -m streamlit run .\Tokenization\project2_tokenizer_streamlit.py

# Project 3 – top 5 most common words (bar chart)
python -m streamlit run .\Tokenization\project3_tokenizer_streamlit.py

# Project 4 – your sentence tokenizer variant
python -m streamlit run .\Tokenization\project4_tokenizer_streamlit.py

# Project 5 – remove English stopwords (option to keep negations)
python -m streamlit run .\Tokenization\project5_stopwords_streamlit.py

# Project 6 – top 5 words (punctuation excluded)
python -m streamlit run .\Tokenization\project6_top_words_streamlit.py
```

Tips:

* If the default port is busy: add `--server.port 8502`
* Stop the app: **Ctrl + C**

## How to run (plain Python scripts)

```powershell
# NLTK word/sentence demo
python .\Tokenization\word_sent_tokenize.py

# Naive split examples
python .\Tokenization\using_split.py

# spaCy tokens + POS + NER
python .\Tokenization\spacy_tokenizer.py

# Remove punctuation & numbers
python .\Tokenization\Removing_p_n.py

# End-to-end cleaning (lowercase, regex, no punct/numbers, stopwords)
python .\Tokenization\text_cleaning_demo.py
```

## What each project shows

* **Project 1:** Sentence tokenization with `nltk.sent_tokenize()`, total sentence count, first & last word display.
* **Project 2:** Tokenizer UI baseline (task-2 style) for experimenting with inputs.
* **Project 3 / 6:** Compute token frequencies and render a **Top-5 words** bar chart (punctuation removed, lower-cased).
* **Project 5:** Remove **English stopwords** with an option to **keep negations** (`no/not/nor/n’t`) for sentiment use-cases.
* **spaCy demo:** Fast, production-oriented pipeline—tokens, POS tags, and named entities.

## Notes

* The repo **excludes** `.venv/`, caches, and large binaries via `.gitignore`.
* If you accidentally staged the venv:
  `git rm -r --cached .venv && git commit -m "Stop tracking venv"`

---

### Save this README and push (commands)

```powershell
cd "C:\Users\puroh\Downloads\NLP\NLP_1"
@'
# NLP_1 – Tokenization & Text Cleaning (Streamlit + NLTK + spaCy)

Small, focused projects to learn core NLP preprocessing:
- sentence/word tokenization
- stopword removal
- punctuation/number cleaning
- top-word frequency charts
- quick spaCy POS/NER demo

## Folder structure
```

Tokenization/
project1\_tokenizer\_streamlit.py        # Sentence tokenizer + count + first/last word
project2\_tokenizer\_streamlit.py        # Streamlit tokenizer demo (task 2 baseline)
project3\_tokenizer\_streamlit.py        # Top-5 most common words (bar chart)
project4\_tokenizer\_streamlit.py        # Sentence tokenizer variant (saved by you as Project 4)
project5\_stopwords\_streamlit.py        # Remove English stopwords (+ keep-negations option)
project6\_top\_words\_streamlit.py        # Top-5 words bar chart (punctuation removed)
project\_tokenizer\_streamlit.py         # General tokenizer playground
word\_sent\_tokenize.py                  # NLTK word/sentence tokenize (script)
using\_split.py                         # Naive .split() examples
spacy\_tokenizer.py                     # spaCy tokens + POS + entities
Removing\_p\_n.py                        # Remove punctuation & numbers
text\_cleaning\_demo.py                  # Lowercase, regex clean, stopwords pipeline
requirements.txt

````

## Quick start (Windows + PowerShell)

```powershell
cd "C:\Users\puroh\Downloads\NLP\NLP_1"
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
python -m spacy download en_core_web_sm
````

## Run (Streamlit)

```powershell
python -m streamlit run .\Tokenization\project1_tokenizer_streamlit.py
python -m streamlit run .\Tokenization\project2_tokenizer_streamlit.py
python -m streamlit run .\Tokenization\project3_tokenizer_streamlit.py
python -m streamlit run .\Tokenization\project4_tokenizer_streamlit.py
python -m streamlit run .\Tokenization\project5_stopwords_streamlit.py
python -m streamlit run .\Tokenization\project6_top_words_streamlit.py
```

## Run (scripts)

```powershell
python .\Tokenization\word_sent_tokenize.py
python .\Tokenization\using_split.py
python .\Tokenization\spacy_tokenizer.py
python .\Tokenization\Removing_p_n.py
python .\Tokenization\text_cleaning_demo.py
```

## Notes

* `.venv/` and large binaries are ignored via `.gitignore`.
  '@ | Set-Content -Encoding UTF8 README.md

git add README.md
git commit -m "Add README with setup and run instructions"
git push

```

Want me to tweak any descriptions (e.g., what Project 2 specifically does in your version)?
::contentReference[oaicite:0]{index=0}
```

# Tokenization/text_cleaning_demo.py
# Basic text-cleaning utilities + a small demo.
# Requires: nltk  (punkt + stopwords)

import re
from typing import Iterable, List, Tuple, Dict

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# one-time downloads (safe to keep here)
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

# ---------- regex helpers ----------

DEFAULT_REGEX_STEPS: Tuple[Tuple[str, str], ...] = (
    # remove URLs
    (r"https?://\S+|www\.\S+", " "),
    # remove emails
    (r"\b[\w\.-]+@[\w\.-]+\.\w+\b", " "),
    # remove HTML tags
    (r"<.*?>", " "),
    # remove Twitter-style mentions/hashtags
    (r"[@#]\w+", " "),
    # normalize multiple spaces
    (r"\s+", " "),
)

def regex_clean(text: str, steps: Iterable[Tuple[str, str]] = DEFAULT_REGEX_STEPS) -> str:
    """Apply (pattern -> replacement) steps sequentially."""
    cleaned = text
    for pattern, repl in steps:
        cleaned = re.sub(pattern, repl, cleaned)
    return cleaned.strip()

# ---------- core cleaning steps ----------

def to_lower(text: str) -> str:
    return text.lower()

def remove_punct_numbers(text: str, keep_apostrophes: bool = True) -> str:
    """
    Remove punctuation and digits.
    If keep_apostrophes=True, keep ' and - (so don't, co-op stay intact).
    """
    if keep_apostrophes:
        pattern = r"[^A-Za-z\s'\-]"  # keep letters, spaces, apostrophes, hyphens
    else:
        pattern = r"[^A-Za-z\s]"     # keep only letters and spaces
    cleaned = re.sub(pattern, " ", text)
    return " ".join(cleaned.split())

def remove_stopwords(
    tokens: List[str],
    keep_negations: bool = True,
    extra_remove: Iterable[str] | None = None,
    keep: Iterable[str] | None = None,
) -> Tuple[List[str], List[str]]:
    """
    Remove English stopwords from token list.
    Returns (cleaned_tokens, removed_tokens).
    """
    sw = set(stopwords.words("english"))
    if keep_negations:
        sw -= {"no", "not", "nor", "n't"}
    if keep:
        sw -= {w.lower() for w in keep}
    if extra_remove:
        sw |= {w.lower() for w in extra_remove}

    cleaned = [t for t in tokens if t.lower() not in sw]
    removed = [t for t in tokens if t.lower() in sw]
    return cleaned, removed

# ---------- full pipeline ----------

def clean_text_pipeline(
    text: str,
    do_lower: bool = True,
    do_regex: bool = True,
    drop_punct_numbers: bool = True,
    keep_apostrophes: bool = True,
    drop_stopwords: bool = True,
    keep_negations: bool = True,
) -> Dict[str, object]:
    """
    Full cleaning pipeline. Returns a dict with intermediate outputs.
    """
    original = text

    step1 = to_lower(original) if do_lower else original
    step2 = regex_clean(step1) if do_regex else step1
    step3 = remove_punct_numbers(step2, keep_apostrophes=keep_apostrophes) if drop_punct_numbers else step2

    # tokenize (keep only tokens with at least one letter/number)
    tokens = [t for t in word_tokenize(step3) if any(ch.isalnum() for ch in t)]

    if drop_stopwords:
        cleaned_tokens, removed_sw = remove_stopwords(tokens, keep_negations=keep_negations)
    else:
        cleaned_tokens, removed_sw = tokens, []

    return {
        "original": original,
        "lower": step1,
        "regex_cleaned": step2,
        "no_punct_numbers": step3,
        "tokens": tokens,
        "cleaned_tokens": cleaned_tokens,
        "removed_stopwords": removed_sw,
        "removed_stopwords_count": len(removed_sw),
    }

# ---------- demo ----------
if __name__ == "__main__":
    sample = """Hello!!! This is a TEST email: user@example.com.
    Visit https://example.org for more info. We don't remove 'don't' or co-op if requested.
    #NLP @you — Numbers 123 and punctuation!!!"""

    out = clean_text_pipeline(
        sample,
        do_lower=True,
        do_regex=True,
        drop_punct_numbers=True,
        keep_apostrophes=True,
        drop_stopwords=True,
        keep_negations=True,
    )

    print("Original:\n", out["original"], "\n")
    print("After regex:\n", out["regex_cleaned"], "\n")
    print("No punct/numbers:\n", out["no_punct_numbers"], "\n")
    print("Tokens:\n", out["tokens"], "\n")
    print("Cleaned tokens:\n", out["cleaned_tokens"], "\n")
    print("Removed stopwords (count =", out["removed_stopwords_count"], "):\n", out["removed_stopwords"])

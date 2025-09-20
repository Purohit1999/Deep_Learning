# 2. Removing Punctuation & Numbers

# --- Method 1: using string + isdigit() ---
import string

text = "hello!!! I have 2 cats."

# keep only chars that are not punctuation and not digits
cleaned = ''.join(
    char for char in text
    if char not in string.punctuation and not char.isdigit()
)
print(cleaned)   # -> "hello I have  cats"

# (optional) collapse any double spaces created by removals
cleaned_compact = ' '.join(cleaned.split())
print(cleaned_compact)  # -> "hello I have cats"


# --- Alternative using regex ---
import re

# keep only letters (a–z, A–Z) and whitespace; drop everything else
cleaned_regex = re.sub(r'[^A-Za-z\s]', '', text)
print(cleaned_regex)        # -> "hello I have  cats"
print(' '.join(cleaned_regex.split()))  # -> "hello I have cats"

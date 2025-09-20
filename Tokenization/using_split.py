text = "Hello there! Welcome to NLP. Let's learn together."

# Simple split on spaces
words = text.split()
print("Using split():", words)

# Naive sentence split
sentences = text.split(".")
print("Using split('.'):", sentences)

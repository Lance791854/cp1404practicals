"""
Word Occurrences
Estimate: 20 minutes
Actual:   17 minutes
"""

user_words = input("Text: ")
word_count = {}
words = user_words.split()
max_size = max(len(word) for word in words)

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word:{max_size}} : {count}")

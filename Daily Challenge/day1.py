'''
Challenge: "Word Frequency Counter"

Goal:
Write a Python program that counts how many times each word appears in a given sentence — ignoring punctuation and capitalization.

Example Input:

sentence = "Hello world, hello ChatGPT! The world is big, and the world is round."


Expected Output:

{'hello': 2, 'world': 3, 'chatgpt': 1, 'the': 2, 'is': 2, 'big': 1, 'and': 1, 'round': 1}


Requirements:

Convert all words to lowercase.

Ignore punctuation (e.g., commas, periods, exclamation marks).

Output a dictionary of words and their counts.

You can only use basic Python — no external libraries like collections.Counter.

Hints (optional, if you get stuck):

You can use .replace() or re.sub() to remove punctuation.

.split() can help separate words.

A dictionary is your best friend here.
'''

import re

sentence = "Hello world, hello ChatGPT! The world is big, and the world is round."

no_comma = re.sub(r"[,!]", "", sentence)

split_word = no_comma.split()

word_counter = {}

for word in split_word:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

print(word_counter)
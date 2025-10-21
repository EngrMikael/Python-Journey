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

# `import re` is importing the regular expression module in Python. This module allows you to work
# with regular expressions, which are powerful tools for pattern matching and text manipulation. In
# this specific case, `re` is used to remove punctuation from the input sentence using the `re.sub()`
# function.
import re

# The line `sentence = "Hello world, hello ChatGPT! The world is big, and the world is round."` is
# assigning a string to the variable `sentence`. The string contains a sentence with words separated
# by spaces and punctuation marks like commas and exclamation marks. This sentence will be used as
# input for the word frequency counter program.
sentence = "Hello world, hello ChatGPT! The world is big, and the world is round."

# The line `no_comma = re.sub(r"[,!]", "", sentence)` is using the `re.sub()` function from the `re`
# module to remove commas and exclamation marks from the `sentence` string.
no_comma = re.sub(r"[,!]", "", sentence)

# `split_word = no_comma.split()` is splitting the modified sentence `no_comma` into a list of words.
# The `split()` method is called on the `no_comma` string, which separates the string into a list of
# words based on whitespace (spaces). This creates a list where each element is a word from the
# sentence without any commas or exclamation marks.
split_word = no_comma.split()

# `word_counter = {}` is initializing an empty dictionary named `word_counter`. This dictionary will
# be used to store the count of each word in the input sentence. Each word encountered in the sentence
# will be a key in the dictionary, and the corresponding value will be the frequency of that word in
# the sentence.
word_counter = {}

# This part of the code is iterating over each word in the `split_word` list, which contains all the
# words from the input sentence without punctuation.
for word in split_word:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

# `print(word_counter)` is displaying the contents of the `word_counter` dictionary, which contains
# the count of each word in the input sentence. When this line is executed, it will output the
# dictionary showing each unique word as a key and the number of times it appears in the sentence as
# the corresponding value.
print(word_counter)
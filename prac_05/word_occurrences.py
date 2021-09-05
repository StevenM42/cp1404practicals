"""
CP1404/CP5632 Practical
Count word frequency from an input sentence
"""

sentence = input("Text: ")
words = sentence.split()
word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

counted_words = list(word_frequency.keys())
counted_words.sort()

for word in counted_words:
    print("{} : {}".format(word, word_frequency[word]))

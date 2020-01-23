# IMPORTS
from random import randint, sample

poem = open("poem.txt", 'r')

poem_lines = poem.readlines()
poem_lines = [word.rstrip('\n') for word in poem_lines] 
poem_words = []

for i in poem_lines:
    words = i.split()
    poem_words.append(words)

print(poem_words)
# sentence = ' '.join(poem_words)
# print(sentence)
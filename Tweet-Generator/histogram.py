# IMPORTS
import sys

# poem = open(sys.argv[1], 'r')

# if len(sys.argv[1]) == 1:
#     poem = open(sys.argv[1], 'r')
# else:
#     poem_words = sys.argv[1:]

poem = open('poem.txt', 'r')
poem_lines = poem.read().lower()
poem_words = poem_lines.split()

def histogram(source):
    hist = {}
    for i in source:
        hist[i] = hist.get(i, 0) + 1
        print(i, ' => ', hist[i])

histogram(poem_words)


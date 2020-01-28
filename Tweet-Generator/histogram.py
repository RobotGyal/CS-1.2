# IMPORTS
poem = open("poem.txt", 'r')
poem_lines = poem.read().lower()
poem_words = poem_lines.split()

def histogram(source):
    hist = {}
    for i in source:
        hist[i] = hist.get(i, 0) + 1
    return hist

print(histogram(poem_words))
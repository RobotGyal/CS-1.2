import sys
poem = open("poem.txt", 'r')
poem_lines = poem.read().lower()
poem_words = poem_lines.split()

def frequency(word, histogram):
    num = histogram.count(word)
    return num

print(frequency(sys.argv[1], poem_words))
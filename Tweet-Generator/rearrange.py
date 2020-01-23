import sys
import random

def printing_at_random(words):
    random.shuffle(words)
    length = len(words)
    for i in range(0, length): 
        print (words[i], end=" ")

printing_at_random(sys.argv[1:])
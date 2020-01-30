import random

poem = open("poem.txt", 'r')
poem_lines = poem.read().lower()
poem_words = poem_lines.split()

def sample(source):
    count = 0
    for i in range(len(source)):
        j=0
        for j in range(i):
            if (source[i] == source[j]):
                break
        if (i == j + 1): 
            count += 1
            print(source[i], " = ", round(((source.count(source[i])/count)*100), 2), '%')


sample(poem_words)
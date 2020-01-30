
poem = open("poem.txt", 'r')
poem_lines = poem.read().lower()
poem_words = poem_lines.split()


def unique_words(histogram):
    count = 0
    for i in range(len(histogram)):
        j=0
        for j in range(i):
            if (histogram[i] == histogram[j]):
                break
        if (i == j + 1): 
            count += 1
    return count

print(unique_words(poem_words))

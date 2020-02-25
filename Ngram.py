# words = "Be who you are and say what you feel, because those who mind don't matter and those who matter don't mind."
words = "how much wood would a woodchuck chuck if a woodchuck could chuck wood."
order = 3
ngrams= {}

i=0
for i in range(len(words)-order):
    grams = words[i:i+3]   #takes in 3 characters at a time
    # ngrams.setdefault(grams, 0) # Insert key with a value of default if key is not in the dictionary
    # ngrams[grams]+=1  # increase value count if found again
    if grams not in ngrams.keys():
        ngrams[grams]=[]
    ngrams[grams].append(words[i+3])

# print(ngrams)
[print(key, value) for key, value in ngrams.items()]
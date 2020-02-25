from random import randrange, choice

# words = "Be who you are and say what you feel, because those who mind don't matter and those who matter don't mind."
words = "how much wood would a woodchuck chuck if a woodchuck could chuck wood."
order = 3
ngrams= {}


# MAIN NGRAM FUNCTION
i=0
for i in range(len(words)-order):
    grams = words[i:i+3]   #takes in 3 characters at a time
    # ngrams.setdefault(grams, 0) # Insert key with a value of default if key is not in the dictionary
    # ngrams[grams]+=1  # increase value count if found again
    if grams not in ngrams.keys():
        ngrams[grams]=[] #make empty if not in ngram
    ngrams[grams].append(words[i+3]) #print next possible char (from ngram[gram[0]])

# [print(key, value) for key, value in ngrams.items()]
# print(n_gram(words, order))    #for function refactoring 



# SENTENCE GENERATION
# current_gram = words[0:3]
# possibilities = ngrams[current_gram]
# _next = random(possibilities)
# result = current_gram+_next


test = 50
current_gram = words[0:3]
result = current_gram
for _ in range(test):
    if current_gram not in ngrams.keys():
        break
    possibilities = ngrams[current_gram]
    _next = possibilities[randrange(len(possibilities))]
    result += _next
    current_gram = result[len(result)-order:len(result)]
    print(current_gram, end=" ")

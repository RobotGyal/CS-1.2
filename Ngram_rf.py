from random import randrange, choice

# words = "Be who you are and say what you feel, because those who mind don't matter and those who matter don't mind."
# words = "how much wood would a woodchuck chuck if a woodchuck could chuck wood."

with open('everything.txt', 'r') as file:
    words = file.read().replace('\n', '')


# order = 6
# ngrams= {}


# MAIN NGRAM FUNCTION
def n_gram(corpus, order, ngrams=None):
    if ngrams is None:
        ngrams ={}
    i=0
    for i in range(len(words)-order):
        grams = words[i:i+order]   #takes in 3 characters at a time
        # ngrams.setdefault(grams, 0) # Insert key with a value of default if key is not in the dictionary
        # ngrams[grams]+=1  # increase value count if found again
        if grams not in ngrams.keys():
            ngrams[grams]=[] #make empty if not in ngram
        ngrams[grams].append(words[i+order]) #print next possible char (from ngram[gram[0]])
    return ngrams

# [print(key, value) for key, value in ngrams.items()]  # printing all ngrams
# print(n_gram(words, order))    #for function refactoring 
# print(n_gram(words, 6))

ngrams=n_gram(words, 2)

# # SENTENCE GENERATION
def generate_sentence(corpus, order, runs, ngrams):
    # runs = 200
    current_gram = words[0:order]  #start at beginning
    result = current_gram
    for _ in range(runs):
        if current_gram not in ngrams.keys():   # keyError handling
            break
        possibilities = ngrams[current_gram]  #all possibilities
        _next = possibilities[randrange(len(possibilities))]   #choose a random one from possibilities
        result += _next   #add to result
        current_gram = result[len(result)-order:len(result)]   # next 3 of the currently picked gram
    return result

print(generate_sentence(words, 2, 200, ngrams))
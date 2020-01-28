# IMPORTS
from random import randint, sample

words = open("/usr/share/dict/words", 'r')

dictionary_words = words.readlines()

rand_amount = randint(1, 12)
random_dictionary_words = sample(dictionary_words, rand_amount)
random_dictionary_words = [word.rstrip('\n') for word in random_dictionary_words] 

sentence = ' '.join(random_dictionary_words)
print(sentence)


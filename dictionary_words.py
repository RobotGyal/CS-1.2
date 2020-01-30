# IMPORTS
from random import randint, sample
from flask import request
import app

words = open("/usr/share/dict/words", 'r')

dictionary_words = words.readlines()

def pick_words(dictionary_words, num):
    # rand_amount = randint(1, 12)
    random_dictionary_words = sample(dictionary_words, num)
    random_dictionary_words = [word.rstrip('\n') for word in random_dictionary_words] 
    sentence = ' '.join(random_dictionary_words)
    return sentence


# print(pick_words(dictionary_words))


from flask import Flask, render_template, request, url_for
from random import randrange, choice, randint
import histogram
import dictionary_words
import Ngram_rf


app = Flask(__name__)

# poem = open("poem2.txt", 'r')
# poem_lines = poem.read().lower()
# poem_words = poem_lines.split()

# @app.route('/')
# def hello():
#     random_num = random.randint(1, len(poem_words))
#     words = request.args.get('words', default = 1, type = int)  # number of words to be displayed from url query
#     sentence = dictionary_words.pick_words(poem_words, words)  # put words together into a sentence
#     return render_template('index.html', sentence=sentence, random_num=random_num)


with open('wind_corpus.txt', 'r') as file:
    words = file.read().replace('\n', '')

ngrams=Ngram_rf.n_gram(words, 6)


@app.route('/')
def home():
    random_runs = randint(1, 300)
    # runs = request.args.get('runs', default = 20, type = int)  # number of runs to do
    sentence = Ngram_rf.generate_sentence(words, 6, random_runs, ngrams)
    return render_template('index.html', sentence=sentence, random_runs=random_runs)



if __name__ == '__main__':
    app.run(debug=True)
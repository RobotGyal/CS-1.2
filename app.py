from flask import Flask, render_template, request, url_for
import random
import histogram
import dictionary_words


app = Flask(__name__)

poem = open("poem2.txt", 'r')
poem_lines = poem.read().lower()
poem_words = poem_lines.split()


@app.route('/')
def hello():
    random_num = random.randint(1, len(poem_words))
    words = request.args.get('words', default = 1, type = int)  # number of words to be displayed from url query
    sentence = dictionary_words.pick_words(poem_words, words)  # put words together into a sentence
    return render_template('index.html', sentence=sentence, random_num=random_num)

if __name__ == '__main__':
    app.run(debug=True)
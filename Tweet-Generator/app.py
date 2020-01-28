from flask import Flask
from histogram import histogram
app = Flask(__name__)


poem = open("poem.txt", 'r')
poem_lines = poem.read().lower()
poem_words = poem_lines.split()



@app.route('/')
def data(poem_words):
    return histogram(poem_words)
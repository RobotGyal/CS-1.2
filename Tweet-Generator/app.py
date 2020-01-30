from flask import Flask, render_template, request
import random
import histogram


app = Flask(__name__)

poem = open("poem2.txt", 'r')
poem_lines = poem.read().lower()
poem_words = poem_lines.split()



test = histogram.histogram(poem_words)


@app.route('/')
def hello():
    hello = 'hello world'
    return render_template('index.html', hello=hello, test=test)




if __name__ == '__main__':
    app.run(debug=True)
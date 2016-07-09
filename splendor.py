from flask import Flask
from flask import render_template
import random
import os

app = Flask(__name__)


@app.route('/')
def splendor():
    return display_card_at_random()


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def display_card_at_random():
    base_dir = os.path.dirname(__file__)
    lookup_dir = os.path.join(base_dir, 'static/cards')
    all_cards = list(listdir_nohidden(lookup_dir))
    filename = random.choice(all_cards)
    return render_template('splendor.html', card=filename)


@app.route('/choose_card', methods=['GET', 'POST'])
def choose_card():
    return display_card_at_random()


if __name__ == '__main__':
    app.run()

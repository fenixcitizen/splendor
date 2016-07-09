from flask import Flask
from flask import render_template
import random
import os

app = Flask(__name__)

all_cards = []

@app.route('/')
def splendor():
    return display_cards_at_random()

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def display_cards_at_random():
    card1 = random.choice(all_cards)
    card2 = random.choice(all_cards)
    card3 = random.choice(all_cards)
    card4 = random.choice(all_cards)
    return render_template('splendor.html', cards=[card1, card2, card3, card4])


@app.route('/choose_card', methods=['GET', 'POST'])
def choose_card():
    return display_cards_at_random()


def load_all_cards():
    global all_cards
    base_dir = os.path.dirname(__file__)
    lookup_dir = os.path.join(base_dir, 'static/cards')
    all_cards = list(listdir_nohidden(lookup_dir))

if __name__ == '__main__':
    load_all_cards()
    app.run()

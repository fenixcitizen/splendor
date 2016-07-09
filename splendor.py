from flask import Flask
from flask import render_template
import random
import os

app = Flask(__name__)

all_cards = []
first_row_cards = []


def initialize_game():
    global all_cards
    base_dir = os.path.dirname(__file__)
    lookup_dir = os.path.join(base_dir, 'static/cards')
    all_cards = list(listdir_nohidden(lookup_dir))
    initialize_first_row()


def initialize_first_row():
    card1 = random.choice(all_cards)
    card2 = random.choice(all_cards)
    card3 = random.choice(all_cards)
    card4 = random.choice(all_cards)
    global first_row_cards
    first_row_cards = [card1, card2, card3, card4]


@app.route('/')
def display_game():
    return render_template('splendor.html', cards=first_row_cards)


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


@app.route('/choose_card', methods=['GET', 'POST'])
def choose_card():
    global first_row_cards
    for card in first_row_cards
        if card == request.data
    first_row_cards[0] = random.choice(all_cards)
    return display_game()


if __name__ == '__main__':
    initialize_game()
    app.run()

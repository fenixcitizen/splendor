from flask import Flask, request, jsonify
from flask import render_template
import random
import os

app = Flask(__name__)

all_cards = []
level3_cards = []
level2_cards = []
level1_cards = []


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
    card5 = random.choice(all_cards)
    card6 = random.choice(all_cards)
    card7 = random.choice(all_cards)
    card8 = random.choice(all_cards)
    card9 = random.choice(all_cards)
    card10 = random.choice(all_cards)
    card11 = random.choice(all_cards)
    card12 = random.choice(all_cards)
    global level1_cards
    global level2_cards
    global level3_cards
    level1_cards = [card1, card2, card3, card4]
    level2_cards = [card5, card6, card7, card8]
    level3_cards = [card9, card10, card11, card12]


@app.route('/')
def display_game():
    return render_template('splendor.html', level1_cards=level1_cards, level2_cards=level2_cards, level3_cards=level3_cards)

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

@app.route('/choose_card_ajax')
def choose_card_ajax():
    global level1_cards
    global level2_cards
    global level3_cards
    card_info = request.args.get('card_info')
    for x in range(0,2):
        if level1_cards[x] == card_info:
            level1_cards[x+1] = random.choice(all_cards)
    return jsonify(result=random.choice(all_cards))

if __name__ == '__main__':
    initialize_game()
    app.run()

#initialize game
#choose starting player

#flask_tests
#mainly clicks on tokens and cards
  #click on card (option take_hand or take_game)
  #click on draw_card (always take gold)
  #click on token_draw (only allows to take same once)
  #token taken is in transition area
  #payment optional with gold
  #setting to never pay with gold (although I may want to pay with gold to block colour for another player)

#value
#colour
#points

#card
#level
#cost (value list)
#bonus (value)

#card_holder
#current card
#location (display | display draw | player_game | player_hand, transition)
#player (PlayerA, PlayerB, null)
#level (Level1, Level2, Level3, null)

#noble
#requirements (value list)
#points

#noble holder
#location (player | display)
#player (PlayerA, PlayerB, null)

#token
#type (colour)

#token holder
#location (display, player, transition)
#type (colour)
#count

#player
#token holders (for each colour)
#hand (card holders)
#game (card holders)
#points
#name

#game
#turn_number
#players
#current_player
#display_draw (levels)
#display_cards (levels)
#display_nobles
#tokens
#is last turn

#allow cost and bonus in gold
#allow ability to destroy other player cards or return them to hands
#release as a game

#player decides on noble before or after the card is replenished?
#end nobles, discard tokens, replenish

#test
  #user_action
  #game_update

#first no display / no UI
#ideally works as a class without even the WEB UI so can be tested without
#independent class -> web server wrapper -> UI
#HTML5
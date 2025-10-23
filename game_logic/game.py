from utils.deck import create_deck
from utils.deck import shuffle
from utils.deck import compare_cards

def create_player(name :str = 'AI'):
    player = {}
    player['name'] = name
    player['hand'] = []
    player['won_pile'] = []
    return player


def init_game():
    player_1 = create_player('Efraim')
    player_2 = create_player()
    deck = shuffle(create_deck())
    player_1['hand'] = deck[0:26]
    player_2['hand'] = deck[26:]

    return  {"deck": deck, "player_1" : player_1, "player_2" : player_2}

def play_round(p1:dict,p2:dict):
    print('Play round')
    card_p1 = p1['hand'].pop()
    card_p2 = p2['hand'].pop()
    compare = compare_cards(card_p1, card_p2)
    if compare == 'p1':
        p1['won_pile'].append(card_p1)
        p1['won_pile'].append(card_p2)
        print(f'\n\n\n{p1['name']} win in this round\n{'-' * 25}\n\n\n{p1['name']} take {card_p1} and {card_p2}\n\n\n')
    elif compare == 'p2':
        p2['won_pile'].append(card_p1)
        p2['won_pile'].append(card_p2)
        print(f'\n\n\n{p2['name']} win in this round\n{'-' * 25}\n\n\n{p2['name']} take {card_p1} and {card_p2}\n\n\n')
    if compare == 'WAR':
        print(f'\n\n\nWAR\n{'-' * 3}\n\n\n')
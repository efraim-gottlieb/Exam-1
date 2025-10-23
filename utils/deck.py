from random import randint

def create_card(rank:str,suite:str):
    special_ranks = {"J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    card = {}
    card["rank"] = rank
    card["suite"] = suite
    if rank in special_ranks.keys():
        card["value"] = special_ranks[rank]
    else:
        card["value"] = int(rank)
    return card

def compare_cards(p1_card:dict, p2_card:dict):
    if p1_card['value'] > p2_card['value']:
        return 'p1'
    if p1_card['value'] < p2_card['value']:
        return 'p2'
    return 'WAR'

def create_deck():
    deck = []
    for suit in ["H", "C", "D", "S"]:
        for special_rank in ['J', 'Q', 'K', 'A']:
            deck.append(create_card(special_rank, suit))
        for i in range(2,11):
            deck.append(create_card(i, suit))
    return deck

def shuffle(deck:list[dict]):
    for _ in range(1000):
        card_1 = randint(0,len(deck) -1)
        card_2 = randint(0,len(deck) -1)
        deck[card_1], deck[card_2] = deck[card_2], deck[card_1]
    return deck




# ===================================== TESTS ===================================== #
# card_1 = create_card('K', 'H')
# card_2 = create_card('A', 'H')
# print(compare_cards(card_1, card_2))

# print(shuffle([card_1,card_2]))
print('lendeck ....', shuffle(create_deck()))
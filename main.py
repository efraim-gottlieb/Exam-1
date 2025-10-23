from game_logic.game import init_game
from game_logic.game import play_round

def main():
    print(f'\n\n{'=' * 10} Game start {'=' * 10}\n\n\n')
    game = init_game()
    while game['player_1']['hand'] and game['player_2']['hand']:
        input('Press Enter to play a round ')
        play_round(game['player_1'], game['player_2'])

    winner = max(len(game['player_1']['won_pile']), len(game['player_2']['won_pile']))
    if len(game['player_1']['won_pile']) > len(game['player_2']['won_pile']):
        winner = game["player_1"]['name']
    elif len(game['player_1']['won_pile']) < len(game['player_2']['won_pile']):
        winner = game["player_2"]['name']

    print(f'{'=' * 30}\n{' ' * 10}Game Over\n{' ' * 9}{'-' * 11}')
    if len(game['player_1']['won_pile']) == len(game['player_2']['won_pile']):

        print(f'\n{' ' * 11}DRAW !')
    else:
        print(f'\n{' ' * 6}{winner} win the game !')

if __name__ == '__main__':
    main()
    while 1 :
        input()

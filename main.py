from game_logic.game import init_game
from game_logic.game import play_round

def main():
    game = init_game()
    while game['player_1']['hand'] and game['player_2']['hand']:
        play_round(game['player_1'], game['player_2'])

    winner = max(len(game['player_1']['won_pile']), len(game['player_2']['won_pile']))
    if len(game['player_1']['won_pile']) > len(game['player_2']['won_pile']):
        winner = game["player_1"]['name']
    elif len(game['player_1']['won_pile']) < len(game['player_2']['won_pile']):
        winner = game["player_2"]['name']

    print(f'{'=' * 30}\n{' ' * 10}Game Over')
    if len(game['player_1']['won_pile']) == len(game['player_2']['won_pile']):
        print('DRAW')
    else:
        print(f'{winner} win the game')

main()
from functools import reduce
from math import sqrt

input_data = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

with open('adventofcode20/day22_input.txt', 'r') as f:    
    input_data = f.read()


deck1, deck2 = input_data.split('\n\n')
deck1 = [int(i) for i in deck1.split('\n')[1:]]
deck2 = [int(i) for i in deck2.split('\n')[1:]]

def play_game(deck1, deck2):
    states = []
    while deck1 and deck2:
        state = '-'.join([str(i) for i in deck1 + [0] + deck2])
        if state in states:
            winner = 1
            break
        else:
            states.append(state)
        play1 = deck1.pop(0)
        play2 = deck2.pop(0)
        
        if play1 <= len(deck1) and play2 <= len(deck2):
            round_winner, _ = play_game(deck1[:play1], deck2[:play2])
            if round_winner == 1:
                deck1.extend([play1, play2])
            else:
                deck2.extend([play2, play1])
        elif play1 > play2:
            deck1.extend([play1, play2])
        elif play2 > play1:
            deck2.extend([play2, play1])
    else:
        winner = 1 if deck1 else 2
    deck = deck1 if winner == 1 else deck2
    res = 0
    for i, x in enumerate(deck[::-1]):
        res += (i+1)*x

    return winner, res

w, res = play_game(deck1, deck2)
print('Score:', res)

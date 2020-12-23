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

print(deck1)
print(deck2)

while deck1 and deck2:
    play1 = deck1.pop(0)
    play2 = deck2.pop(0)
    
    if play1 > play2:
        deck1.extend([play1, play2])
    elif play2 > play1:
        deck2.extend([play2, play1])

winner = deck1 if deck1 else deck2
res = 0
for i, x in enumerate(winner[::-1]):
    res += (i+1)*x
print('Score:', res)

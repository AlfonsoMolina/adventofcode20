from itertools import product
from copy import deepcopy
input_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

with open('adventofcode20/day11_input.txt', 'r') as f:    
    input_data = f.read()

layout = [[c for c in line] for line in input_data.split('\n')]
key = ''.join(c for line in input_data for c in line)

previous_key = ''

def get_surroundings(coord,  layout):
    y, x = coord
    for i, j in product([-1, 0, 1],repeat=2):
        if i == 0 and j == 0:
            continue
        if 0 <= y+j < len(layout) and 0 <= x+i < len(layout[y]):
            yield layout[y+j][x+i]
        
def get_tiles(layout):
    for y in range(len(layout)):
        for x in range(len(layout[y])):
            yield y, x, layout[y][x]

while key != previous_key:
    new_layout = deepcopy(layout)
    for y, x, tile in get_tiles(layout):
        total_seats = sum(1 for t in get_surroundings([y,x], layout) if t == '#')
        if tile == 'L' and total_seats == 0:
            new_layout[y][x] = '#'
        elif tile == '#' and total_seats >= 4:
            new_layout[y][x] = 'L'
    layout = new_layout
    previous_key = key
    key = ''.join(c for line in layout for c in line)

for row in layout:
    print(''.join(row))

print(sum(1 for row in layout for tile in row if tile == '#'))
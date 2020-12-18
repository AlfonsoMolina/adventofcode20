from itertools import product
from copy import deepcopy
from collections import defaultdict

input_data = """\
.#.
..#
###"""

with open('adventofcode20/day17_input.txt', 'r') as f:    
    input_data = f.read()

layout = defaultdict(lambda: defaultdict(dict))

z = 0
y = 0
x = 0

for row in input_data.split('\n'):
    x = 0
    for column in row:
        layout[z][y][x] = column
        x += 1
    y += 1

def print_layout(layout):
    z_borders = [min(layout.keys()), max(layout.keys())+1]
    y_borders = [min(min(layout[z].keys()) for z in layout) ,
                 max(max(layout[z].keys()) for z in layout) +1]
    x_borders = [min(min(layout[z][y].keys()) for z in layout for y in layout[z] if layout[z][y].keys()),
                 max(max(layout[z][y].keys()) for z in layout for y in layout[z] if layout[z][y].keys()) +1]

    for z in range(*z_borders):
        print('LAYER: ', z)
        for y in range(*y_borders):
            row = ''
            for x in range(*x_borders):
                try:
                    tile = layout[z][y][x]
                except KeyError:
                    tile = '.'
                row = row + tile
            print(row)

def get_surroundings(coord, layout):
    z, y, x = coord
    for i, j, u in product([-1, 0, 1],repeat=3):
        if i == 0 and j == 0 and u == 0:
            continue
        try:
            tile = layout[z+u][y+j][x+i]
            yield tile
        except KeyError:
            continue

def count_actives(layout):
    count = 0
    for z in layout:
        for y in layout[z]:
            for x in layout[z][y]:
                if layout[z][y][x] == '#':
                    count += 1
    return count

# print_layout(layout)

for n in range(6):
    print('STEP ' + str(n))
    # Borders to test, accounting with the +2 needed for range
    z_borders = [min(layout.keys())-1, max(layout.keys())+2]
    y_borders = [min(min(layout[z].keys()) for z in layout) -1,
                 max(max(layout[z].keys()) for z in layout) +2]
    x_borders = [min(min(layout[z][y].keys()) for z in layout for y in layout[z] if layout[z][y].keys()) -1,
                 max(max(layout[z][y].keys()) for z in layout for y in layout[z] if layout[z][y].keys()) +2]

    new_layout = deepcopy(layout)

    for z in range(*z_borders):
        for y in range(*y_borders):
            for x in range(*x_borders):
                try:
                    tile = layout[z][y][x]
                    # print(z, y, x, tile)
                except KeyError:
                    tile = '.'
                active_cubes = sum(1 for t in get_surroundings([z,y,x], layout) if t == '#')
                if tile == '#' and not 2 <= active_cubes <= 3:
                    new_layout[z][y][x] = '.'
                    # print(z, y, x, 'becomes inactive with ', active_cubes, ' neighboots')
                elif tile == '.' and active_cubes == 3:
                    new_layout[z][y][x] = '#'
                    # print(z, y, x, 'becomes active with ', active_cubes)
    layout = new_layout
    # print_layout(layout)
    # input()
    
print(count_actives(layout))


from itertools import product
from copy import deepcopy
from collections import defaultdict

input_data = """\
.#.
..#
###"""

with open('adventofcode20/day17_input.txt', 'r') as f:    
    input_data = f.read()

layout = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))

w = 0
z = 0
y = 0
x = 0

for row in input_data.split('\n'):
    x = 0
    for column in row:
        layout[w][z][y][x] = column
        x += 1
    y += 1

def count_active_neighbors(coord, layout):
    w, z, y, x = coord
    count = 0
    for i, j, u, v in product([-1, 0, 1],repeat=4):
        if i == 0 and j == 0 and u == 0 and v == 0:
            continue
        try:
            if layout[w+v][z+u][y+j][x+i] == '#':
                count += 1
        except KeyError:
            continue
    return count

def count_actives(layout):
    count = 0
    for w in layout:
        for z in layout[w]:
            for y in layout[w][z]:
                for x in layout[w][z][y]:
                    if layout[w][z][y][x] == '#':
                        count += 1
    return count

# print_layout(layout)

def minn(something):
    if something:
        return min(something)
    else:
        return 0
def maxx(something):
    if something:
        return max(something)
    else:
        return 0

for n in range(6):
    print('STEP ' + str(n))
    # Borders to test, accounting with the +2 needed for range
    w_borders = [minn(layout.keys())-1, maxx(layout.keys())+2]
    z_borders = [minn(minn(layout[w].keys()) for w in layout) -1,
                 maxx(maxx(layout[w].keys()) for w in layout) +2]
    y_borders = [minn(minn(layout[w][z].keys()) for w in layout for z in layout[w]) -1,
                 maxx(maxx(layout[w][z].keys()) for w in layout for z in layout[w]) +2]
    x_borders = [minn(minn(layout[w][z][y].keys()) for w in layout for z in layout[w] for y in layout[w][z]) -1,
                 maxx(maxx(layout[w][z][y].keys()) for w in layout for z in layout[w] for y in layout[w][z]) +2]

    new_layout = deepcopy(layout)
    for w in range(*w_borders):
        for z in range(*z_borders):
            for y in range(*y_borders):
                for x in range(*x_borders):
                    try:
                        tile = layout[w][z][y][x]
                        # print(z, y, x, tile)
                    except KeyError:
                        tile = '.'
                    active_cubes = count_active_neighbors([w,z,y,x], layout) 
                    if tile == '#' and not 2 <= active_cubes <= 3:
                        new_layout[w][z][y][x] = '.'
                        # print(z, y, x, 'becomes inactive with ', active_cubes, ' neighboots')
                    elif tile == '.' and active_cubes == 3:
                        new_layout[w][z][y][x] = '#'
                        # print(z, y, x, 'becomes active with ', active_cubes)
    layout = new_layout
    # print_layout(layout)
    # input()
    
print(count_actives(layout))


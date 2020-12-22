from functools import reduce
from math import sqrt

input_data = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

with open('adventofcode20/day20_input.txt', 'r') as f:    
    input_data = f.read()

tiles = {}
tiles_borders = {}
for tile in input_data.split('\n\n'):
    tile_id = tile.split('\n')[0][5:-1]
    tiles[tile_id] = [row for row in tile.split('\n')[1:]]

    # Borders read clockwise
    border0 = tiles[tile_id][0]
    border2 = tiles[tile_id][-1][::-1]
    border3 = ''.join([c[0] for c in tiles[tile_id]])[::-1]
    border1 = ''.join([c[-1] for c in tiles[tile_id]])
    tiles_borders[tile_id] = [border0, border1, border2, border3]

# Image will be 3x3 or 12x12 
side = int(sqrt(len(tiles)))
sorted_image = [[0 for j in range(side)] for i in range(side)]

# Look up borders that do not line up with any two other tiles
# Find the first corner
tiles_ids = [t for t in tiles]
neighboors = {}
corner = 0
for i, t in enumerate(tiles_ids):
    neighboors[t] = []
    for j, tt in enumerate(tiles_ids):
        if t == tt:
            continue
        borders1 = tiles_borders[t]
        borders2 = tiles_borders[tt]
        if any(b == bb or b[::-1] == bb for b in borders1 for bb in borders2):
            neighboors[t].append(tt)
    if len(neighboors[t]) == 2 and not corner: #Corner
        corner = t

# Lets put the first corner on position 0, 0:
sorted_image[0][0] = corner
sorted_image[0][1] = neighboors[corner][1]
sorted_image[1][0] = neighboors[corner][0]

# Put each shard on the right place
for y in range(side):
    for x in range(side):
        if sorted_image[y][x]:
            continue
        needed = 4
        placed = []
        if x == 0 or x == side - 1:
            needed -= 1
        if x != 0:
            placed.append(sorted_image[y][x-1])
        if y == 0 or y == side - 1:
            needed -= 1
        if y != 0:
            placed.append(sorted_image[y-1][x])

        # Look up for a tile whose neighboors len is needed and placed are there
        for t, n in neighboors.items():
            if len(n) == needed and all(p in n for p in placed):
                # If it is already placed, look for another one
                if not any(t in row for row in sorted_image):
                    sorted_image[y][x] = t

# Useful function for later
def transform_img(tiles, tid, rotate, flip):
    tile = tiles[tid][:]
    for _ in range(rotate):
        t = tile[:]
        for i in range(len(tile)):
            tile[i] = ''.join([c[i] for c in t])[::-1]
    if flip:
        for i in range(len(tile)):
            tile[i] = tile[i][::-1]
    tiles[tid] = tile

    # Update the borders
    border0 = tile[0]
    border2 = tile[-1][::-1]
    border3 = ''.join([c[0] for c in tile])[::-1]
    border1 = ''.join([c[-1] for c in tile])

    tiles_borders[tid] = [border0, border1, border2, border3]

# Lets rotate the tiles. 
# First, rotate the first corner 
rotate = 0
flip = False
for i, corner_border in enumerate(tiles_borders[corner]):
    if any(corner_border == bb or corner_border[::-1] == bb for bb in tiles_borders[neighboors[corner][0]]):
        # Not a frontier
        continue
    elif any(corner_border == bb or corner_border[::-1] == bb for bb in tiles_borders[neighboors[corner][1]]):
        # Not a frontier
        continue
    else:
        # Border with the unknown. I will put it on the 0. Rotate clockwise.
        rotate = 4 - i
        # Now check next border...
        border = tiles_borders[corner][i - 1]
        if any(corner_border == bb for bb in tiles_borders[neighboors[corner][0]]) or any(corner_border == bb for bb in tiles_borders[neighboors[corner][1]]):
            # Succes, no need to flip
            pass
        else:
            flip = True
        break
transform_img(tiles, corner, rotate, flip) 

# Now transform all the other tiles
for y in range(side):
    for x in range(side):
        if y == 0 and x == 0:
            continue
        rotate = 0
        flip = False
        tile_id = sorted_image[y][x]
        current_borders = tiles_borders[tile_id]
        # If there is a column at left use it as a reference point
        if x > 0:
            target = sorted_image[y][x-1]
            for i, b in enumerate(current_borders):
                if any((tmp := b) == bb or (tmp := b[::-1]) == bb for bb in tiles_borders[target]):
                    # Success. Border in position i should be at 3.
                    # It needs 3 - i rotations 
                    rotate = 3 - i
                    # Since I read the borders clockwise, it should be always oppsed
                    if any(b == bb for bb in tiles_borders[target]):
                        flip = True
                        rotate += 2
                    break
        # If not, use a row above it.
        elif y > 0:
            target = sorted_image[y-1][x]
            for i, b in enumerate(current_borders):
                if any(b == bb or b[::-1] == bb for bb in tiles_borders[target]):
                    # Success. Border in position i should be at 0.
                    # It needs 4 - i rotations
                    rotate = (4 - i) % 4
                    if any(b == bb for bb in tiles_borders[target]):
                        flip = True
                    break
        transform_img(tiles, tile_id, rotate, flip) 

final_map = []
for y in range(side):
    for yy in range(1, len(tiles[tile_id])-1):
        row = ''.join([tiles[sorted_image[y][x]][yy][1:-1] for x in range(side)])
        # print(row)
        final_map.append(row)



def look_for_monsters(sea ):
    monsters_found = 0
    sea_monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ']
    for i in range(len(sea)-2):
        for o in range(len(sea[0]) - len(sea_monster[0]) +2):
            for j in [0, 1, 2]:
                if not all(sea[i+j][k+o] == '#' for k, t in enumerate(sea_monster[j]) if t == '#'):
                    break
            else:
                for j in [0, 1, 2]:
                    for k, t in enumerate(sea_monster[j]):
                        if t == '#':
                            sea[i+j] = sea[i+j][:k+o] + 'O' + sea[i+j][k+o+1:]
                monsters_found += 1
    return monsters_found



# Useful function for later
def transform_sea(img, rotate, flip):
    for _ in range(rotate):
        tmp = img[:]
        for i in range(len(img)):
            img[i] = ''.join([c[i] for c in tmp])[::-1]
    if flip:
        for i in range(len(img)):
            img[i] = img[i][::-1]
    return img



for i in range(10):
    monster_count = look_for_monsters(final_map)
    if monster_count != 0:
        break
    final_map = transform_sea(final_map, 0, True)
    monster_count = look_for_monsters(final_map)
    if monster_count != 0:
        break
    final_map = transform_sea(final_map, 0, True)
    final_map = transform_sea(final_map, 1, False)



total = ''.join(final_map).count('#') 




for y in range(len(final_map)):
    print(final_map[y])

print(monster_count, total)

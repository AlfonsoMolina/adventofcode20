from functools import reduce

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

    border1 = tiles[tile_id][0]
    border3 = tiles[tile_id][-1]
    border2 = ''.join([c[0] for c in tiles[tile_id]] )
    border4 = ''.join([c[-1] for c in tiles[tile_id]] )
    tiles_borders[tile_id] = [border1, border2, border3, border4]


# Look up borders that do not line up with any two other tiles
tiles_ids = [t for t in tiles]
candidates = []
for i, t in enumerate(tiles_ids):
    found = 0
    for j, tt in enumerate(tiles_ids):
        if t == tt:
            continue
        borders1 = tiles_borders[t]
        borders2 = tiles_borders[tt]
        if any(b == bb or b[::-1] == bb for b in borders1 for bb in borders2):
            found += 1
    if found == 2: #Corner
        candidates.append(int(t))

print(candidates)
res = reduce((lambda x, y: x* y), candidates)
print(res)
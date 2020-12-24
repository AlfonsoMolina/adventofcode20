from copy import deepcopy

input_data = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

with open('adventofcode20/day24_input.txt', 'r') as f:    
    input_data = f.read()
lines = input_data.split('\n')

def flip_tile(tiles, coord):
    if coord not in tiles:
        tiles[coord] = True
    else:
        tiles[coord] = not tiles[coord]
    # # Prepare surrounding cells
    y = int(coord.split(',')[0])
    x = int(coord.split(',')[1])
    neighboors = [[1,1], [-1,-1], [1,-1], [-1,1], [2,0], [-2,0]]
    for n in neighboors:
        coord = str(y + n[1]) + ',' + str(x + n[0])
        if coord not in tiles:
            tiles[coord] = False

tiles = {}
for line in lines:
    i = 0
    x = 0
    y = 0
    while True:
        if i >= len(line):
            coord = str(y) + ',' + str(x)
            flip_tile(tiles, coord)
            break
        c = line[i]
        if c in 'ns':
            i += 1
            c += line[i]

        # Move
        if c == 'e':
            x += 2
        elif c == 'se':
            y -= 1
            x += 1
        elif c == 'sw':
            y -= 1
            x -= 1
        elif c == 'w':
            x -= 2
        elif c == 'nw':
            y += 1
            x -= 1
        elif c == 'ne':
            y += 1
            x += 1
        
        i += 1

print(sum([1 for v in tiles.values() if v]))

def get_surroundings(tiles, coord):
    y = int(coord.split(',')[0])
    x = int(coord.split(',')[1])
    neighboors = [[1,1], [-1,-1], [1,-1], [-1,1], [2,0], [-2,0]]
    res = 0
    for n in neighboors:
        coord = str(y + n[1]) + ',' + str(x + n[0])
        if coord in tiles and tiles[coord]:
            res += 1
    return res

for i in range(1, 101):
    new_tiles = deepcopy(tiles)
    for coord, black in tiles.items():
        surr = get_surroundings(tiles, coord)
        if not black and surr == 2:
            flip_tile(new_tiles, coord)
        elif black and (surr == 0 or surr > 2):
            flip_tile(new_tiles, coord)
    tiles = new_tiles
    if i % 10 == 0:
        print(sum([1 for v in tiles.values() if v]))

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

# with open('adventofcode20/day24_input.txt', 'r') as f:    
#     input_data = f.read()
lines = input_data.split('\n')

tiles = {}
for line in lines:
    i = 0
    x = 0
    y = 0
    while True:
        if i >= len(line):
            coord = str(y) + ',' + str(x)
            if coord not in tiles:
                tiles[coord] = True
            else:
                tiles[coord] = not tiles[coord]
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

print(tiles)
res = 0
res = sum([1 for v in tiles.values() if v])
print(res)
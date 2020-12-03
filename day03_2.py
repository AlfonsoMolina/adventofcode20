input_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

with open('adventofcode20/day03_input.txt', 'r') as f:    
    input_data = f.read()

input_data = [[ch for ch in line] for line in input_data.split('\n')]

slope = [3, 1]


def use_slope(forest, slope):
    pos = [0,0]
    tree_count = 0
    while pos[0] < len(forest):
        y, x = pos
        tree_count += 1 if forest[y][x] == '#' else 0
        y = y + slope[1]
        x = (x + slope[0]) % len(forest[0]) 
        pos = [y, x]
    return tree_count

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
tree_count = 1
for slope in slopes:
    tree_count *= use_slope(input_data, slope)
print(tree_count)
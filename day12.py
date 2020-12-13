input_data = """F10
N3
F7
R90
F11"""

with open('adventofcode20/day12_input.txt', 'r') as f:    
    input_data = f.read()

input_data = input_data.split('\n')

position = [0, 0]
facing = 'E'

for line in input_data:
    action, n = line[0], int(line[1:])
    
    if action == 'F':
        action = facing

    if action in 'N':
        position[0] += n
    elif action == 'S':
        position[0] -= n
    elif action == 'E':
        position[1] += n
    elif action == 'W':
        position[1] -= n

    if action in 'LR':
        coord = 'NESW'
        curr = coord.find(facing)
        new = n // 90
        new = curr + new if action == 'R' else curr - new
        new = new %4
        facing = coord[new]

print(position)
print(abs(position[0]) + abs(position[1]))
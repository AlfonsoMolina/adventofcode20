input_data = """F10
N3
F7
L270
F11"""

with open('adventofcode20/day12_input.txt', 'r') as f:    
    input_data = f.read()

input_data = input_data.split('\n')

ship = [0, 0]           # NS, EW
waypoint = [1, 10]      # NS, EW
region = 0 # 0 = NE, 1 = SE, 2 = SW, 3 = NW
region_coord = {0:[1,1], 1:[-1, 1], 2:[-1,-1], 3:[1,-1]}


for line in input_data:
    action, n = line[0], int(line[1:])
    
    if action == 'F':
        ship[0] += n * waypoint[0]
        ship[1] += n * waypoint[1]
    elif action in 'N':
        waypoint[0] += n
    elif action == 'S':
        waypoint[0] -= n
    elif action == 'E':
        waypoint[1] += n
    elif action == 'W':
        waypoint[1] -= n

    if action in 'RL':
        if action == 'L':
            n = 360-n
        
        curr_region = 0
        for region, values in region_coord.items():
            if waypoint[0] * values[0] >= 0 and waypoint[1] * values[1] >= 0:
                curr_region = region
                break

        new_region = (curr_region + n // 90) % 4
        if (n // 90) % 2:
            waypoint = [waypoint[1], waypoint[0]]
        
        waypoint = [region_coord[new_region][0] * abs(waypoint[0]), 
                    region_coord[new_region][1] * abs(waypoint[1])]
        
print(ship)
print(abs(ship[0]) + abs(ship[1]))
from itertools import product
from copy import deepcopy
input_data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

with open('adventofcode20/day14_input.txt', 'r') as f:    
    input_data = f.read()

lines = [line.split() for line in input_data.split('\n')]
memory = {}
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
for line in lines:
    if line[0] == 'mask':
        mask = line[-1]
    else:
        address = line[0][4:-1]
        value = int(line[-1])

        # Replace 1 
        value = value | int(mask.replace('X', '0'),2)
        # Rpelace 0
        value = value & int(mask.replace('X', '1'),2)
        memory[address] = value


print(sum(memory.values()))
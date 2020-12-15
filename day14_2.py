from itertools import product
from copy import deepcopy
input_data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

with open('adventofcode20/day14_input.txt', 'r') as f:    
    input_data = f.read()

lines = [line.split() for line in input_data.split('\n')]
memory = {}
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
for line in lines:
    if line[0] == 'mask':
        mask = line[-1]
    else:
        address = int(line[0][4:-1])
        value = int(line[-1])

        # Replace 1 
        address = address | int(mask.replace('X', '0'),2)
        
        # Replace all X into all combinations...
        for floating_x in product([1,0], repeat=mask.count('X')):
            # Look only into the X
            temp_mask = mask.replace('1', 'f').replace('0', 'f')
            temp_address = address
            for x in floating_x:
                index = temp_mask.find('X')
                temp_mask = temp_mask[:index] + str(x) + temp_mask[index+1:]
            temp_address = temp_address | int(temp_mask.replace('f', '0'),2)
            temp_address = temp_address & int(temp_mask.replace('f', '1'),2)
            memory[temp_address] = value
        
print(sum(memory.values()))
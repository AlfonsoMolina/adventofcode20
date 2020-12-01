from itertools import permutations

input_data = """1721
979
366
299
675
1456"""

with open('adventofcode20/day01_input.txt', 'r') as f:    
    input_data = f.read()

input_data = input_data.split('\n')

data = [int(d) for d in input_data if d]

res = 0

for i, j in permutations(data, 2):
    if i + j == 2020:
        res = i*j
        break

print(res)

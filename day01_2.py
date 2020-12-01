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

for i, j, k in permutations(data, 3):
    if i + j + k == 2020:
        res = i*j*k
        break

print(res)

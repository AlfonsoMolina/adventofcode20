input_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

with open('adventofcode20/day09_input.txt', 'r') as f:    
    input_data = f.read()

input_data = [int(i) for i in input_data.split('\n')]

group_size = 25

for i in range(group_size, len(input_data)):
    if not any(j + k == input_data[i] for j in input_data[i-25:i] for k in input_data[i-25:i] if j != k):
        print(i, input_data[i])
        break
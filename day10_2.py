input_data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

with open('adventofcode20/day10_input.txt', 'r') as f:    
    input_data = f.read()

input_data = [int(i) for i in input_data.split('\n')]
input_data.append(max(input_data)+3)
input_data.append(0)
input_data.sort(reverse=True)

number_of_paths = {}
number_of_paths[input_data[0]] = 1

print(input_data)
# Walk the outlets from bigger to smaller, counting the number of paths
for i in range(1, len(input_data)):
    outlet = input_data[i]
    paths = 0

    # The number of paths that a number offer is the sum of all the paths
    # of the numbers it can reach
    for prev in input_data[i-3 if i > 3 else 0:i]:
        if prev - outlet <= 3:
            paths += number_of_paths[prev]
    number_of_paths[outlet] = paths

print(number_of_paths[0])
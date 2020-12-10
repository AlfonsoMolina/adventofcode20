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
input_data.append(0)
input_data.sort()
input_data.append(input_data[-1]+3)

differences = [i[1] - i[0] for i in zip(input_data, input_data[1:])]

print('1: ', differences.count(1))
print('2: ', differences.count(2))
print('3: ', differences.count(3))
print('4: ', differences.count(4))
print(differences.count(1) * differences.count(3))